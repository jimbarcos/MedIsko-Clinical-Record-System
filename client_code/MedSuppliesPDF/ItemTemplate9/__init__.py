from ._anvil_designer import ItemTemplate9Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import data_access
import datetime

class ItemTemplate9(ItemTemplate9Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAudit= data_access.cacheInventory()
    self.initDisplay()

  def initDisplay(self):
    now = datetime.datetime.now()
    format = now.strftime("%B %d, %Y")
    expformat = self.item["expiryDate"].strftime("%B %d, %Y")
    self.outlined_1.text = format
    self.outlined_1_copy.text = self.item["medicineMaterial"]
    self.outlined_1_copy_2.text = self.item["quantity"]
    self.outlined_1_copy_3.text = self.item["consumed"]
    self.outlined_1_copy_4.text = self.item["quantity"] - self.item["consumed"]
    self.outlined_1_copy_5.text = expformat
    # Any code you write here will run before the form opens.
