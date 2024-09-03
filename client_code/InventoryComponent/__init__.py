from ._anvil_designer import InventoryComponentTemplate
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


class InventoryComponent(InventoryComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.myInventory = data_access.cacheInventory()
    self.repeating_panel_1.items = self.myInventory.search(tables.order_by('items', ascending = True))
    #self.visibleGeneratePDF()
    self.visibleCard1()
    
    self.myInventoryHistory = data_access.cacheInventoryHistory()
    self.repeating_panel_2.items = self.myInventoryHistory.search(tables.order_by('filename', ascending=False))
    self.visibleCard2()


    # Any code you write here will run before the form opens.

  def visibleGeneratePDF(self):
    if (not self.repeating_panel_1.items) or self.repeating_panel_1.items is None or len(self.repeating_panel_1.items) == 0:
      self.btnGeneratePDF.visible = False
      self.outlined_card_5.visible = False
    else:
      self.btnGeneratePDF.visible = True
      self.outlined_card_5.visible = True
    pass

  def visibleCard1(self):
    if not self.btnGeneratePDF.visible:
      self.outlined_card_1.visible = False
      self.label_2.visible = False
    else:
      self.outlined_card_1.visible = True
      self.label_2.visible = True

  def visibleCard2(self):
    if (not self.repeating_panel_2.items) or self.repeating_panel_2.items is None or len(self.repeating_panel_2.items) == 0:
      self.outlined_card_2.visible = False
    else:
      self.outlined_card_2.visible = True
    
  def btnInventory_click(self, **event_args):
    self.myInventory.add_row()
    navigation.go_inventory()
    pass

  def drop_down_1_change(self, **event_args):
   orientation = None
   if self.drop_down_1.selected_value == 'Ascending Alphabetical':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('items', ascending = True))
   elif self.drop_down_1.selected_value == 'Descending Alphabetical':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('items', ascending = False))
   elif self.drop_down_1.selected_value == 'Quantity':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('quantity', ascending = False))
   elif self.drop_down_1.selected_value == 'Serviceable':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('serviceable', ascending = False))
   elif self.drop_down_1.selected_value == 'Repair':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('forRepair', ascending = False))
   elif self.drop_down_1.selected_value == 'Condemn':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('forCondemn', ascending = False))
   elif self.drop_down_1.selected_value == 'Replacement':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('needReplacement', ascending = False))
   elif self.drop_down_1.selected_value == 'Additional':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('additional', ascending = False))
   elif self.drop_down_1.selected_value == 'Quantity of Request':
      orientation = self.repeating_panel_1.items = self.myInventory.search(tables.order_by('quantityRequest', ascending = False))

   return orientation
  pass

  def btnGeneratePDF_click(self, **event_args):
    uuid4 = uuid.uuid4()
    pdf = anvil.server.call('create_pdf')
    created_date = datetime.datetime.now()
    formatted_date = created_date.strftime("%B %d, %Y (%I-%M %p)")
    file_name = f"Medical Equipments Inventory – {formatted_date}.pdf"
    named_pdf = anvil.BlobMedia('application/pdf', pdf.get_bytes(), name=file_name)
    
    
    self.saveHistory = anvil.server.call('displayInventoryHistory')
    recordID = 'fileinventoryID - '  + str(uuid4)
    self.saveHistory.add_row(filename=file_name, fileVersion=named_pdf, fileInventoryID = recordID)

    anvil.media.download(named_pdf)
    navigation.go_inventory()
   # self.saveHistory.get(fileInventoryID).
  
    pass

