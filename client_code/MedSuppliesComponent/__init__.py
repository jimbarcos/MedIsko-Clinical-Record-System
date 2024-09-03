from ._anvil_designer import MedSuppliesComponentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import data_access
from .. import navigation
import uuid
import datetime

class MedSuppliesComponent(MedSuppliesComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAudit = data_access.cacheAudit()
    self.myAuditHistory = data_access.cacheInventoryAudit()
    self.repeating_panel_1.items =  self.myAudit.search(tables.order_by('medicineMaterial', ascending=True))
    self.repeating_panel_2.items =  self.myAuditHistory.search(tables.order_by('filename', ascending=False))
    self.visibleCard2()
    #self.visibleGeneratePDF()
    # Any code you write here will run before the form opens.


  def visibleGeneratePDF(self):
    if (not self.repeating_panel_1.items) or self.repeating_panel_1.items is None or len(self.repeating_panel_1.items) == 0:
      self.btnGeneratePDF.visible = False
      self.label_3.visible = False
    else:
      self.btnGeneratePDF.visible = True
      self.label_3.visible = True
    pass

  def visibleCard2(self):
    if (not self.repeating_panel_2.items) or self.repeating_panel_2.items is None or len(self.repeating_panel_2.items) == 0:
      self.outlined_card_5.visible = False
    else:
      self.outlined_card_5.visible = True
  
  def btnAnalgesic_click(self, **event_args):
    self.myAudit.add_row()
    navigation.go_medsupplies()
    pass

  def drop_down_1_change(self, **event_args):
    if self.drop_down_1.selected_value == 'Medicine/Material':
      self.repeating_panel_1.items = self.myAudit.search(tables.order_by('medicineMaterial', ascending = True))
    elif self.drop_down_1.selected_value == 'Type':
      self.repeating_panel_1.items = self.myAudit.search(tables.order_by('type', ascending = True))  
    elif self.drop_down_1.selected_value == 'Quantity':
      self.repeating_panel_1.items = self.myAudit.search(tables.order_by('quantity', ascending = False))
    elif self.drop_down_1.selected_value == 'Consumed':
      self.repeating_panel_1.items = self.myAudit.search(tables.order_by('consumed', ascending = False))
    elif self.drop_down_1.selected_value == 'Expiry Date':
      self.repeating_panel_1.items = self.myAudit.search(tables.order_by('expiryDate', ascending = True))
    pass

  def verifyInput (self):
    error = False
    
    if not self.date_picker_1.date:
      Notification('Please fill out the Date').show()
      error = True
      return error
      
    if self.text_box_1_copy_3.text == '' or self.text_box_1_copy_3.text is None:
      Notification('Please fill out the First Name Details').show()
      error = True
      return error

    if self.text_box_1_copy_2_copy.text == '' or self.text_box_1_copy_2_copy.text is None:
      Notification('Please fill out the Last Name Details').show()
      error = True
      return error

    if self.text_box_1_copy.text == '' or self.text_box_1_copy.text is None:
      Notification('Please fill out the Position Details').show()
      error = True
      return error

    if self.text_box_1_copy_2.text == '' or self.text_box_1_copy_2.text is None:
      Notification('Please fill out the Unit Department Details').show()
      error = True
      return error
    
    return error
    
  def btnGeneratePDF_click(self, **event_args):
    error = self.verifyInput()

    if error:
      return
    else:
      uuid4 = uuid.uuid4()
      
      created_date = datetime.datetime.now()
      date = self.date_picker_1.date
      dateFormat = date.strftime("%B %d, %Y")
      
      anvil.server.call('passAuditDate', dateFormat)
      anvil.server.call('passAuditPhysicianFirstName', self.text_box_1_copy_3.text)
      anvil.server.call('passAuditPhysicianLastName', self.text_box_1_copy_2_copy.text)
      anvil.server.call('passAuditUnit', self.text_box_1_copy_2.text)
      anvil.server.call('passAuditPosition', self.text_box_1_copy.text)
      pdf = anvil.server.call('create_pdfAudit')
      
      formatted_date = created_date.strftime("%B %d, %Y (%I-%M %p)")
      file_name = f"Medicine/Materials Audit Inventory – {formatted_date}.pdf"
      named_pdf = anvil.BlobMedia('application/pdf', pdf.get_bytes(), name=file_name)
      
      
      self.saveAudit= anvil.server.call('displayInventoryAudit')
      recordID = 'fileAuditID - '  + str(uuid4)
      self.saveAudit.add_row(fileAuditID = recordID,
                             filename=file_name, 
                             fileVersion=named_pdf,
                             physicianFirstName = self.text_box_1_copy_3.text,
                             physicianLastName = self.text_box_1_copy_2_copy.text,
                             physicianPosition = self.text_box_1_copy.text,
                             dateToSubmit = self.date_picker_1.date,
                             unit = self.text_box_1_copy_2.text)
  
      anvil.media.download(named_pdf)
      navigation.go_medsupplies()
    # self.saveHistory.get(fileInventoryID).
  
    pass



