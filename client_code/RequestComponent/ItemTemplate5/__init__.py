from ._anvil_designer import ItemTemplate5Template
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


class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.mySupplies = data_access.cacheRequestSupplies()
    self.initDisplay()
    
  def initDisplay(self):
    self.tbSupplies.text = self.item['suppliesName']
    self.tbQuantity.text = self.item['suppliesQuantity']
    self.dpSupplies.date = self.item['suppliesReceivedDate']
    self.tbRemarks.text = self.item['suppliesRemarks']

  def btnDelete1_click(self, **event_args):
    if confirm('Delete Supply Record?'):
      self.item.delete()
      self.remove_from_parent()
      navigation.go_request()
    pass

  def verifyInput (self):
    error = False

    if self.tbSupplies.text == '' or self.tbSupplies.text is None or not self.tbSupplies.text:
      Notification('Invalid Component: Please Complete the Supplies Details').show()
      error = True
      return error

    if self.tbQuantity.text == '' or self.tbQuantity.text is None or self.tbQuantity.text < 0:
      Notification('Invalid Component: Please Complete the Quantity Details').show()
      error = True
      return error

    if self.dpSupplies.date == '' or self.dpSupplies.date is None or not self.dpSupplies.date:
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
        recordID = 'suppliesID - ' + str(uuid4)
        self.mySupplies.add_row(suppliesName = self.tbSupplies.text, suppliesQuantity = self.tbQuantity.text, suppliesReceivedDate = self.dpSupplies.date, suppliesRemarks = self.tbRemarks.text, suppliesID = recordID)
        Notification('Successfully Saved').show()
        self.item.delete()
        self.remove_from_parent()
        navigation.go_request()
      except wrongEvent as e:
        Notification('Error Inserting the Supply Item. Please try again').show()
    pass
