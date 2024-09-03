from ._anvil_designer import ItemTemplate1Template
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
from .. import InventoryComponent
import uuid

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myInventory = data_access.cacheInventory()
    self.initDisplay()
    
    

  def initDisplay(self):
    self.txtItems.text = self.item['items']
    self.txtQuantity.text = self.item['quantity']
    self.txtServiceable.text = self.item['serviceable']
    self.txtForRepair.text = self.item['forRepair']
    self.txtForCondemn.text = self.item['forCondemn']
    self.txtNeedReplacement.text = self.item['needReplacement']
    self.txtAdditional.text = self.item['additional']
    self.txtQuantityRequest.text = self.item['quantityRequest']

    
    if self.txtItems.text != '':
      self.txtItems.visible = True
      self.dropDownItems.visible = False
    else:
      self.dropDownItems.visible = True
      self.txtItems.visible = False

  def btnItemDelete_click(self, **event_args):
    if confirm('Delete Item Record?'):
      self.item.delete()
      self.remove_from_parent()
      navigation.go_inventory()
    pass

  def dropDownItems_change(self, **event_args):
    if self.dropDownItems.selected_value == 'Others':
      self.txtItems.visible = True
      self.dropDownItems.visible = False
    else:
      self.txtItems.visible = False
      self.dropDownItems.visible = True
    
    pass

  def verifyInput (self):
    #valid_options = ["Stethoscope", "Sphygmomanometer, table, aneroid", "Sphygmomanometer, pocket, aneroid", "Sphygmomanometer with stand", "Oto-ophthalmoscope set", "Thermal Scanner", "Thermoscan (Infrared) with stand", "Nebulizer", "Manual resuscitator, adult", "Minor surgical set", "Aluminum tray with cover", "Aluminum kidney basin", "Oval magnifying lamp with stand", "Finger pulse oximeter", "Oxygen tank with regulator", "Oxygen tank (reserved)", "Oxygen tank carrier", "Portable Oxygen tank with regulator", "Glucometer", "Stretcher, folding", "Wheelchair", "Emergency Trauma Bag", "Dressing cart", "Hospital bed with mattress", "Medicine cabinet", "Weighing Scale unit height and bar type", "Spine board", "ECG machine", "Ice cap", "Ice pack (coleman)", "Ice chest", "Hot water bag", "Towels for ice pack/ice cap", "Bedsheets and pillow cases", "Blankets/linens", "Pillows", "Autoclave", "Sterilizer", "First Aid Kit Bag (PHN)", "Electric airpot", "Computer", "Printer", "Air Purifier", "Ultraviolet Disinfection Light", "Shredder", "Folding Bed (Military Style with Bag)", "Industrial Fan (Iwata) Tripod Feet", "Standard Exhaust Fan", "Others"]
    error = False

    txt_items_empty = not self.txtItems.text
    dropdown_empty = not self.dropDownItems.selected_value
    if txt_items_empty and dropdown_empty:
      Notification('Missing Component: Please Complete the Item Details').show()
      error = True
      return error
    
    if self.txtQuantity.text == '' or self.txtQuantity.text is None or self.txtQuantity.text < 0:
      Notification('Invalid Component: Please Complete the Quantity Details').show()
      error = True
      return error

    if self.txtServiceable.text == '' or self.txtServiceable.text is None or self.txtServiceable.text < 0:
      Notification('Invalid Component: Please Complete the Serviceable Details').show()
      error = True
      return error

    if self.txtForRepair.text == '' or self.txtForRepair.text is None or self.txtForRepair.text < 0:
      Notification('Invalid Component: Please Complete the Repair Details').show()
      error = True
      return error
      
    if self.txtForCondemn.text == '' or self.txtForCondemn.text is None or self.txtForCondemn.text < 0:
      Notification('Invalid Component: Please Complete the Condemn Details').show()
      error = True
      return error

    if self.txtNeedReplacement.text == '' or self.txtNeedReplacement.text is None or self.txtNeedReplacement.text < 0:
      Notification('Invalid Component: Please Complete the Replacement Details').show()
      error = True
      return error

    if self.txtAdditional.text == '' or self.txtAdditional.text is None or self.txtAdditional.text < 0:
      Notification('Invalid Component: Please Complete the Additional Details').show()
      error = True
      return error

    if self.txtQuantityRequest.text == '' or self.txtQuantityRequest.text is None or self.txtQuantityRequest.text < 0:
      Notification('Invalid Component: Please Complete the Quantity of Request Details').show()
      error = True
      return error
    pass
    
  def btnSave_click(self, **event_args):
    error = self.verifyInput()
    if not error:
      self.strItems = ''
      if self.dropDownItems.selected_value == 'Others' or self.txtItems.text != '':
        self.strItems = self.txtItems.text
      else:
        self.strItems = self.dropDownItems.selected_value

      uuid4 = uuid.uuid4()
      recordID = 'inventoryID - ' + str(uuid4)
      
      try:
        self.myInventory.add_row(items=self.strItems, 
                              quantity=self.txtQuantity.text, 
                              serviceable=self.txtServiceable.text, 
                              forRepair=self.txtForRepair.text, 
                              forCondemn=self.txtForCondemn.text, 
                              needReplacement=self.txtNeedReplacement.text, 
                              additional=self.txtAdditional.text, 
                              quantityRequest=self.txtQuantityRequest.text, InventoryID = recordID)
        Notification('Successfully Saved').show()
        self.item.delete()
        self.remove_from_parent()
        navigation.go_inventory()
      except Exception as e:
        Notification('Failed to Save: {}'.format(str(e))).show()
    pass

 
