from ._anvil_designer import ItemTemplate4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import navigation
from ... import data_access
import uuid


class ItemTemplate4(ItemTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myMedicines = data_access.cacheRequestMedicine()
    self.initDisplay()
    
  def initDisplay(self):
    self.tbMedicine.text = self.item['medicineName']
    self.tbQuantity.text = self.item['medicineQuantity']
    self.dpMedicine.date = self.item['medicineReceivedDate']
    self.tbRemarks.text = self.item['medicineRemarks']


  def btnDelete_click(self, **event_args):
    if confirm('Delete Medicine Record?'):
      self.item.delete()
      self.remove_from_parent()
      navigation.go_request()
    pass

  def verifyInput (self):
    error = False

    if self.tbMedicine.text == '' or self.tbMedicine.text is None or not self.tbMedicine.text:
      Notification('Invalid Component: Please Complete the Medicine Details').show()
      error = True
      return error

    if self.tbQuantity.text == '' or self.tbQuantity.text is None or self.tbQuantity.text < 0:
      Notification('Invalid Component: Please Complete the Quantity Details').show()
      error = True
      return error

    if self.dpMedicine.date == '' or self.dpMedicine.date is None or not self.dpMedicine.date:
      Notification('Invalid Component: Please Complete the Date Received Details').show()
      error = True
      return error
      
    if self.tbRemarks.text == '' or self.tbRemarks.text is None or not self.tbRemarks.text:
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
        recordID = 'medicineID - ' + str(uuid4)
        self.myMedicines.add_row(medicineName = self.tbMedicine.text, medicineQuantity = self.tbQuantity.text, medicineReceivedDate = self.dpMedicine.date, medicineRemarks = self.tbRemarks.text, medicineID = recordID)
        Notification('Successfully Saved').show()
        self.item.delete()
        self.remove_from_parent()
        navigation.go_request()
      except wrongEvent as e:
        Notification('Error Inserting the Medicine Item. Please try again').show()
    pass
