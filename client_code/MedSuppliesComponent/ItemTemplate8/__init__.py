from ._anvil_designer import ItemTemplate8Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import data_access
from ... import navigation
import uuid


class ItemTemplate8(ItemTemplate8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAudit = data_access.cacheAudit()
    self.initDisplay()
    
  def initDisplay(self):
    self.txtMedMat.text = self.item['medicineMaterial']
    self.ddType.selected_value = self.item['type']
    self.txtQuantity.text = self.item['quantity']
    self.txtConsumed.text = self.item['consumed']
    self.dateExpiry.date = self.item['expiryDate']

  def btnItemDelete_click(self, **event_args):
      if confirm('Delete Item Record?'):
        self.item.delete()
        self.remove_from_parent()
        navigation.go_medsupplies()


  def verifyInput (self):
    error = False

    if self.txtMedMat.text == '' or self.txtMedMat.text is None or not self.txtMedMat.text:
      Notification('Invalid Component: Please Complete the Medicine/Material Details').show()
      error = True
      return error

    if self.ddType.selected_value == '' or self.ddType.selected_value is None or not self.ddType.selected_value:
      Notification('Invalid Component: Please Complete the Type Details').show()
      error = True
      return error
     
    if self.txtQuantity.text == '' or self.txtQuantity.text is None or self.txtQuantity.text < 0:
      Notification('Invalid Component: Please Complete the Quantity Details').show()
      error = True
      return error

    if self.dateExpiry.date == '' or self.dateExpiry.date is None or not self.dateExpiry.date:
      Notification('Invalid Component: Please Complete the Date Expiry Details').show()
      error = True
      return error
      
    if self.txtConsumed.text == '' or self.txtConsumed.text is None or not self.txtConsumed.text:
      Notification('Invalid Component: Please Complete the Consumed Details').show()
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
        recordID = 'auditID - ' + str(uuid4)
        self.myAudit.add_row(audit_ID = recordID, 
                                 medicineMaterial = self.txtMedMat.text, 
                                 type = self.ddType.selected_value, 
                                 quantity = self.txtQuantity.text, 
                                 consumed = self.txtConsumed.text, 
                                 expiryDate = self.dateExpiry.date)
        Notification('Successfully Saved').show()
        self.item.delete()
        self.remove_from_parent()
        navigation.go_medsupplies()
      except:
        Notification('Error Inserting the Item. Please try again').show()
    pass


