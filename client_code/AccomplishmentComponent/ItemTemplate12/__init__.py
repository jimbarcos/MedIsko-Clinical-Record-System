from ._anvil_designer import ItemTemplate12Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import navigation
import uuid
import datetime
from ... import data_access

class ItemTemplate12(ItemTemplate12Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAccomplishment = data_access.cacheAccomplishment()
    self.initDisplay()
    
  def initDisplay(self):
    self.txtmedicalservices.text = self.item['medicalservices']
    self.ddtype.selected_value = self.item['type']
    self.txtstudents.text = self.item['students']
    self.txtfaculty.text = self.item['faculty']
    self.txtadmin.text = self.item['admin']
    self.txtdependents.text = self.item['dependents']
    self.txtremarks.text = self.item['remarks']


  def btnItemDelete_click(self, **event_args):
    if confirm('Delete Record?'):
      self.item.delete()
      self.remove_from_parent()
      navigation.go_accomplishment()
    pass

  def verifyInput (self):
    error = False

    if self.txtmedicalservices.text == '' or self.txtmedicalservices.text is None or not self.txtmedicalservices.text:
      Notification('Invalid Component: Please Complete the Medical Services Rendered Details').show()
      error = True
      return error

    if self.ddtype.selected_value == '' or self.ddtype.selected_value is None or not self.ddtype.selected_value:
      Notification('Invalid Component: Please Complete the Type Details').show()
      error = True
      return error
     
    if self.txtstudents.text == '' or self.txtstudents.text is None or self.txtstudents.text < 0:
      Notification('Invalid Component: Please Complete the Student Details').show()
      error = True
      return error

    if self.txtadmin.text == '' or self.txtadmin.text is None or self.txtadmin.text < 0:
      Notification('Invalid Component: Please Complete the Admin Details').show()
      error = True
      return error

    if self.txtfaculty.text == '' or self.txtfaculty.text is None or self.txtfaculty.text < 0:
      Notification('Invalid Component: Please Complete the Faculty Details').show()
      error = True
      return error

    if self.txtdependents.text == '' or self.txtdependents.text is None or self.txtdependents.text < 0:
      Notification('Invalid Component: Please Complete the Dependents Details').show()
      error = True
      return error

    if self.txtremarks.text == '' or self.txtremarks.text is None or not self.txtremarks.text:
      Notification('Invalid Component: Please Complete the Remarks Details').show()
      error = True
      return error
    pass
  
  def btnSave_click(self, **event_args):
    error = self.verifyInput()

    if error:
      return
    else:
      try:
        uuid4 = uuid.uuid4()
        recordID = 'accomplishmentID - ' + str(uuid4)
        self.myAccomplishment.add_row(accomplishmentreport_ID = recordID,
                                 medicalservices = self.txtmedicalservices.text,
                                 type = str(self.ddtype.selected_value),
                                 students = self.txtstudents.text,
                                 faculty = self.txtfaculty.text,
                                 admin = self.txtadmin.text,
                                 dependents = self.txtdependents.text,
                                 remarks = self.txtremarks.text)
        Notification('Successfully Saved').show()
        self.item.delete()
        self.remove_from_parent()
        navigation.go_accomplishment()
      except:
        Notification('Error Inserting the Item. Please try again').show()
    pass
