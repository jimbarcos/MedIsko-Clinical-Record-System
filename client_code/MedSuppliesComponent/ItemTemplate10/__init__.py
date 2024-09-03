from ._anvil_designer import ItemTemplate10Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import navigation


class ItemTemplate10(ItemTemplate10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.initDisplay()
    # Any code you write here will run before the form opens.

  def initDisplay(self):
    self.label_1.text = self.item['filename']

  def button_1_click(self, **event_args):
    downloadFile = self.item['fileVersion']
    named_pdf = anvil.BlobMedia('application/pdf', downloadFile.get_bytes(), name=self.label_1.text)
    anvil.media.download(named_pdf)
    pass

  def btnDeletePDF_click(self, **event_args):
    if confirm('Are you sure you want to delete the save PDF Log?\n\nThis Action can\'t be undone'):
      self.item.delete()
      self.remove_from_parent()
      navigation.go_medsupplies()
    pass