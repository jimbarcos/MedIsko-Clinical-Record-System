from ._anvil_designer import AddMeasurementComponentTemplate
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


class AddMeasurementComponent(AddMeasurementComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.assigned = None
    self.date = None
    self.name = None
    self.sex = None
    self.age = 0
    self.weight = 0

    self.counterErrors = 0
    
    # Any code you write here will run before the form opens.

  def btnSave_click(self, **event_args):
    self.counterErrors = 0
    self.labelError.visible = False
    self.labelErrorTitle.visible = False
    self.labelErrorCatch.visible = False
    error = self.sync_data()
    errorCatch = self.sync_data_Catch()

    if error:
      if self.counterErrors > 0:
        self.labelErrorTitle.visible = True

      self.labelError.text = error
      self.labelError.visible = True
      self.labelErrorCatch.text = errorCatch
      self.labelErrorCatch.visible = True
      return

    #print("Saving Data {} {} {} {} {} {}".format(self.assigned, self.date, self.name, self.sex, self.age, self.weight))
    #anvil.server.call('add_record', )
    self.name = self.name.strip()
    self.sex = self.sex.strip()
    self.assigned = self.assigned.strip()
    
    data_access.addRecord(self.date, self.name, self.age, self.weight, self.sex, self.assigned)
    navigation.go_home()
    Notification("Patient Record - Successfully Recorded").show()
    pass

  def sync_data(self):
    self.collateErrors = []
    tab = "       "
    
    if not self.txtBoxAssigned.text:
      self.collateErrors.append(tab + "• Assigned Physician/Nurse is required") 
      self.counterErrors += 1

    if not self.DatePickerDate.date:
      self.collateErrors.append(tab + "• Date is required") 
      self.counterErrors += 1

    if not self.txtBoxName.text:
      self.collateErrors.append(tab + "• Name is required") 
      self.counterErrors += 1

    if not self.DropDownSex.selected_value:
      self.collateErrors.append(tab + "• Sex is required") 
      self.counterErrors += 1

    if not self.txtBoxAge.text:
      self.collateErrors.append(tab + "• Age is required")
      self.counterErrors += 1

    if not self.txtBoxWeight.text:
      self.collateErrors.append(tab + "• Weight is required") 
      self.counterErrors += 1

    return '\n'.join(self.collateErrors)

  def sync_data_Catch(self):
    try:
      self.assigned = self.txtBoxAssigned.text
      self.date = self.DatePickerDate.date
      self.name = self.txtBoxName.text
      self.sex = self.DropDownSex.selected_value
      self.age = int(self.txtBoxAge.text) if self.txtBoxAge.text is not None else None
      self.weight = int(self.txtBoxWeight.text) if self.txtBoxWeight.text is not None else None
    except TypeError as y:
      self.counterErrors += 1
      return 'Invalid Format: Could not Convert Data {}'.format(y)
    except Exception as x:
      self.counterErrors += 1
      return 'Unknown Error {}'.format(x)
      
    return None

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def DropDownSex_change(self, **event_args):
    """This method is called when an item is selected"""
    pass




  
