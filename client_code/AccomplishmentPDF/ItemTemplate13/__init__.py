from ._anvil_designer import ItemTemplate13Template
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


class ItemTemplate13(ItemTemplate13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAccomplishment= data_access.cacheAccomplishment()
    self.initDisplay()
    # Any code you write here will run before the form opens.


  def initDisplay(self):
    self.txtmedservices.text = self.item["medicalservices"]
    self.txtstudents.text = self.item["students"]
    self.txtfaculty.text = self.item["faculty"]
    self.txtadmin.text = self.item["admin"]
    self.txtdependent.text = self.item["dependents"]
    self.txtremarks.text = self.item["remarks"]