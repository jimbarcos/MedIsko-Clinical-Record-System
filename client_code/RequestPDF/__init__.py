from ._anvil_designer import RequestPDFTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import data_access
from .. import RequestComponent



class RequestPDF(RequestPDFTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myMedicine = data_access.cacheRequestMedicine()
    self.mySupplies = data_access.cacheRequestSupplies()
    self.myInfo = data_access.cacheRequestHistory()

    self.repeating_panel_1.items = self.myMedicine.search(tables.order_by('medicineName', ascending=True))
    self.repeating_panel_2.items = self.mySupplies.search(tables.order_by('suppliesName', ascending=True))

    date = anvil.server.call('returnDate')
    campus = anvil.server.call('returnCampus')
    clinic = anvil.server.call('returnClinic')
    self.label_3.text = str(date) + '\n' + clinic + '\n' + campus

    #app_tables.tblrequesthistory.get()
    #dates = [r['name'] for r in self.myInfo.search()]


    # Any code you write here will run before the form opens.
