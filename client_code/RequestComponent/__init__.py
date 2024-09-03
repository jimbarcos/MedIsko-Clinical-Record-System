from ._anvil_designer import RequestComponentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from .. import navigation
from .. import data_access
import datetime
import uuid


class RequestComponent(RequestComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.myMedicines = data_access.cacheRequestMedicine()
    self.mySupplies = data_access.cacheRequestSupplies()
    
    self.repeating_panel_1.items =  self.myMedicines.search(tables.order_by('medicineName', ascending=True))
    self.repeating_panel_2.items = self.mySupplies.search(tables.order_by('suppliesName', ascending=True))


    self.myRequestHistory = data_access.cacheRequestHistory()
    self.repeating_panel_3.items = self.myRequestHistory.search(tables.order_by('filename', ascending=False))
    #self.visibleGeneratePDF()
    self.visibleLogs()
    # Any code you write here will run before the form opens.

  def visibleLogs(self):
    if ((not self.repeating_panel_3.items) or self.repeating_panel_3.items is None or len(self.repeating_panel_3.items) == 0):
      self.outlined_card_5.visible = False
    else:
      self.outlined_card_5.visible = True
      
  def visibleGeneratePDF(self):
    if ((not self.repeating_panel_1.items) or self.repeating_panel_1.items is None or len(self.repeating_panel_1.items) == 0) and ((not self.repeating_panel_2.items) or self.repeating_panel_2.items is None or len(self.repeating_panel_2.items) == 0):
      self.btnGeneratePDF.visible = False
      self.label_3.visible = False
    else:
      self.btnGeneratePDF.visible = True
      self.label_3.visible = True
    pass
    
  def btnSupplies_click(self, **event_args):
    self.mySupplies.add_row()
    navigation.go_request()
    pass

  def btnMedicine_click(self, **event_args):
    self.myMedicines.add_row()
    navigation.go_request()
    pass

  def drop_down_1_change(self, **event_args):
    if self.drop_down_1.selected_value == 'Medicines':
      self.repeating_panel_1.items = self.myMedicines.search(tables.order_by('medicineName', ascending = True))
    elif self.drop_down_1.selected_value == 'Quantity':
      self.repeating_panel_1.items = self.myMedicines.search(tables.order_by('medicineQuantity', ascending = False))  
    elif self.drop_down_1.selected_value == 'Date Received':
      self.repeating_panel_1.items = self.myMedicines.search(tables.order_by('medicineReceivedDate', ascending = False))  
       
    pass

  def drop_down_2_change(self, **event_args):
    if self.drop_down_2.selected_value == 'Supplies':
      self.repeating_panel_2.items = self.mySupplies.search(tables.order_by('suppliesName', ascending = True))
    elif self.drop_down_2.selected_value == 'Quantity':
      self.repeating_panel_2.items = self.mySupplies.search(tables.order_by('suppliesQuantity', ascending = False))  
    elif self.drop_down_2.selected_value == 'Date Received':
      self.repeating_panel_2.items = self.mySupplies.search(tables.order_by('suppliesReceivedDate', ascending = False))  
       
    pass

  def verifyInput (self):
    error = False
    
    if not self.date_picker_1.date:
      Notification('Please fill out the Date').show()
      error = True
      return error
      
    if self.text_box_1.text == '' or self.text_box_1.text is None:
      Notification('Please fill out the Clinic Details').show()
      error = True
      return error

    if self.text_box_1_copy.text == '' or self.text_box_1_copy.text is None:
      Notification('Please fill out the Campus Details').show()
      error = True
      return error
    
    return error
  def btnGeneratePDF_click(self, **event_args):
    error = self.verifyInput()

    if error:
      return
    else:
      uuid4 = uuid.uuid4()
      date = self.date_picker_1.date
      dateFormat = date.strftime("%B %d, %Y")
      anvil.server.call('passDate', dateFormat)
      anvil.server.call('passCampus', self.text_box_1_copy.text)
      anvil.server.call('passClinic', self.text_box_1.text)
      pdf = anvil.server.call('create_pdfRequest')
      
      created_date = datetime.datetime.now()
      formatted_date = created_date.strftime("%B %d, %Y (%I-%M %p)")
      file_name = f"Request For Medicines and Supplies – {formatted_date}.pdf"
      named_pdf = anvil.BlobMedia('application/pdf', pdf.get_bytes(), name=file_name)
      
      
      self.saveHistory = anvil.server.call('displayRequestHistory')
      recordID = 'requestID - '  + str(uuid4) 
      self.saveHistory.add_row(filename=file_name, fileVersion=named_pdf, fileHistoryID= recordID, dateToSubmit = self.date_picker_1.date, campus = self.text_box_1_copy.text, clinic = self.text_box_1.text )

      
      anvil.media.download(named_pdf)
      
      navigation.go_request()
    pass

  def returnDate(self):
    date = self.date_picker_1.date
    return date

  