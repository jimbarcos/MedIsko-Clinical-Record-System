from ._anvil_designer import ItemTemplate6Template
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

class ItemTemplate6(ItemTemplate6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.mySupplies = data_access.cacheRequestSupplies()
    self.initDisplay()

  def initDisplay(self):
    self.txtSupplies.text = self.item["suppliesName"]
    self.tbQuantity.text = self.item["suppliesQuantity"]
    self.tbReceivedDate.text = self.item["suppliesReceivedDate"]
    self.txtRemarks.text = self.item["suppliesRemarks"]
    # Any code you write here will run before the form opens.
