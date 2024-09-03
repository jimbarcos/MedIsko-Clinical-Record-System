import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#


@anvil.server.callable
def displayInventory():
  me = anvil.users.get_user()
  if me:
    return app_tables.tblinventory.client_writable(user=me)

@anvil.server.callable
def addInventory(items, quantity, serviceable, forRepair, forCondemn, needReplacement, additional, quantityRequest):
  me = anvil.users.get_user()
  if not me:
    raise Exception('You must log in to call this method')

  app_tables.tblinventory.add_row(items=items, quantity=quantity, serviceable=serviceable, forRepair=forRepair, forCondemn=forCondemn, needReplacement=needReplacement, additional=additional, quantityRequest=quantityRequest, user=me)


@anvil.server.callable
def displayInventoryHistory():
  me = anvil.users.get_user()
  if me:
    return app_tables.tblinventoryhistory.client_writable(user=me)


@anvil.server.callable
def displayRequestHistory():
  me = anvil.users.get_user()
  if me:
    return app_tables.tblrequesthistory.client_writable(user=me)