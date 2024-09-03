import datetime
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
def record_disp():
  user = anvil.users.get_user()
  if not user:
    return []
    
  records = app_tables.tbladdrecords.search(tables.order_by("RecordDate", ascending=False), User=user)

  return records

@anvil.server.callable
def add_record(record_date, name, age, weight, sex, assignedStaff):
  created_date = datetime.datetime.now()
  user = anvil.users.get_user()

  if not user:
    raise Exception ("You must log in to call this method.")

  app_tables.tbladdrecords.add_row(CreatedDate=created_date, RecordDate=record_date, Name=name, Age=age, Weight=weight, Sex=sex, User=user, AssignedStaff=assignedStaff)
