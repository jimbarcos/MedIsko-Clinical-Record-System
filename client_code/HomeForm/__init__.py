from ._anvil_designer import HomeFormTemplate
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
import anvil.js


class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    self.baseTitle = self.labelTitle.text
    user = data_access.the_user()
    self.set_AccountState(user)
    navigation.home_form = self
    navigation.go_home()

    
   
    # Any code you write here will run before the form opens.

  def Home_click(self, **event_args):
    navigation.go_home()
    pass

  def Records_click(self, **event_args):
    navigation.go_records()
    pass

  def Inventory_click(self, **event_args):
    navigation.go_inventory()
    pass

  def Request_click(self, **event_args):
    navigation.go_request()
    pass

  def linkAccount_click(self, **event_args):
    navigation.go_account()
    pass

  def linkLogOut_click(self, **event_args):
    user = anvil.users.logout()
    self.set_AccountState(user)
    data_access.logout()
    Notification("Log out Successfully").show()
    navigation.refresh_window()
    navigation.go_home()

  def linkRegister_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel = True)
    self.set_AccountState(user)
    navigation.go_home()
    pass

  def linkLogIn_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel = True)
    self.set_AccountState(user)

    if user:
      Notification("Log in Successfully!").show()
    else:
      Notification("Log in Error, Please try Again.").show()

    
    navigation.go_home()
    pass

  def load_cmpt (self, cmpnt):
    self.column_panelHome.clear()
    self.column_panelHome.add_component(cmpnt)

  def set_activeNav(self, state):
    self.Home.role = 'selected' if state == 'home' else None
    self.Records.role = 'selected' if state == 'records' else None
    self.Inventory.role = 'selected' if state == 'inventory' else None
    self.Request.role = 'selected' if state == 'request' else None
    self.linkAccount.role = 'selected' if state == 'account' else None
    self.botQuest.role = 'selected' if state == 'ask' else None
    self.MedsSupplies.role = 'selected' if state == 'medsupplies' else None
    self.Accomplishment.role = 'selected' if state == 'accomplishment' else None
  pass 

  def set_AccountState(self, user):
    #self.linkAccount.visible = user is not None
    self.linkLogOut.visible = user is not None
    self.linkLogIn.visible = user is None
    #self.linkRegister.visible = user is None
  pass

  def botQuest_click(self, **event_args):
    navigation.go_bot()
    pass

  def Supplies_click(self, **event_args):
    navigation.go_inventory()
    pass

  def MedsSupplies_click(self, **event_args):
    navigation.go_medsupplies()
    pass

  def Accomplishment_click(self, **event_args):
    navigation.go_accomplishment()
    pass






    
