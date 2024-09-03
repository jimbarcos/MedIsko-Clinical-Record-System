from ._anvil_designer import AccomplishmentComponentTemplate
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


class AccomplishmentComponent(AccomplishmentComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAccomplishment = data_access.cacheAccomplishment()
    self.myAccomplishmentHistory = data_access.cacheInventoryAccomplishment()
    self.repeating_panel_1.items =  self.myAccomplishment.search(tables.order_by('medicalservices', ascending=True))
    self.repeating_panel_2.items =  self.myAccomplishmentHistory.search(tables.order_by('filename', ascending=False))
    #self.visibleGeneratePDF()
    self.visibleCard2()
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
    self.myAccomplishment.add_row()
    navigation.go_accomplishment()
    pass

  def verifyInput (self):
    error = False
    
    if not self.date_picker_1.date:
      Notification('Please fill out the Date').show()
      error = True
      return error
      
    if self.text_box_1.text == '' or self.text_box_1.text is None:
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
      
      anvil.server.call('passAccomplishmentDate', dateFormat)
      anvil.server.call('passAccomplishmentPhysicianFirstName', self.text_box_1.text)
      anvil.server.call('passAccomplishmentPhysicianLastName', self.text_box_1_copy_2_copy.text)
      anvil.server.call('passAccomplishmentUnit', self.text_box_1_copy_2.text)
      anvil.server.call('passAccomplishmentPosition', self.text_box_1_copy.text)
      
      pdf = anvil.server.call('create_pdfAccomplishment')

      formatted_date = created_date.strftime("%B %d, %Y (%I-%M %p)")
      file_name = f"Accomplishment Report – {formatted_date}.pdf"
      named_pdf = anvil.BlobMedia('application/pdf', pdf.get_bytes(), name=file_name)
  
      self.saveAccomplishment= anvil.server.call('displayInventoryAccomplishment')
      recordID = 'fileAccomplishmentID - '  + str(uuid4)
      self.saveAccomplishment.add_row(fileAccomplishmentID = recordID,
                             filename=file_name, 
                             fileVersion=named_pdf,
                             physicianFirstName = self.text_box_1.text,
                             physicianLastName = self.text_box_1_copy_2_copy.text,
                             physicianPosition = self.text_box_1_copy.text,
                             dateToSubmit = self.date_picker_1.date,
                             unit = self.text_box_1_copy_2.text)
      

      
      anvil.media.download(named_pdf)
      navigation.go_accomplishment()
    pass

  def drop_down_1_change(self, **event_args):
    if self.drop_down_1_copy.selected_value == 'Medical Services Rendered':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('medicalservices', ascending = True))
    elif self.drop_down_1_copy.selected_value == 'Type':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('type', ascending = True))  
    elif self.drop_down_1_copy.selected_value == 'Students':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('students', ascending = False))
    elif self.drop_down_1_copy.selected_value == 'Faculty':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('faculty', ascending = False))
    elif self.drop_down_1_copy.selected_value == 'Admin':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('admin', ascending = False))
    elif self.drop_down_1_copy.selected_value == 'Dependents':
      self.repeating_panel_1.items = self.myAccomplishment.search(tables.order_by('dependents', ascending = True))
    pass
