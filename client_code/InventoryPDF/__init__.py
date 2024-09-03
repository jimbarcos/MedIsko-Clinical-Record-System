from ._anvil_designer import InventoryPDFTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import data_access
from .. InventoryComponent import InventoryComponent
import datetime

class InventoryPDF(InventoryPDFTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myInventory = data_access.cacheInventory()
    self.repeating_panel_1.items = self.myInventory.search(tables.order_by('items', ascending = True))

    now = datetime.datetime.now()
    current_month = now.strftime("%B")
    current_year = now.year
    
    self.label_2.text = (
        'POLYTECHNIC UNIVERSITY OF THE PHILIPPINES\n'
        'Medical Services Department\n'
        'MEDICAL CLINIC / CAMPUS: Mabini Campus College Medical Clinic\n'
        f'As of ({current_month}) {current_year}\n'
        'Date of submission: _______________'
    )
    # Any code you write here will run before the form opens.
