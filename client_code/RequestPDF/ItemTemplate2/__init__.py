from ._anvil_designer import ItemTemplate2Template
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


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myMedicine = data_access.cacheRequestMedicine()
    self.initDisplay()

  def initDisplay(self):
    self.txtMedicine.text = self.item["medicineName"]
    self.tbQuantity.text = self.item["medicineQuantity"]
    self.tbReceivedDate.text = self.item["medicineReceivedDate"]
    self.txtRemarks.text = self.item["medicineRemarks"]

