import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from ..AddMeasurementComponent import AddMeasurementComponent
from ..HomeAnonComponent import HomeAnonComponent
from ..RequestComponent import RequestComponent
from ..InventoryComponent import InventoryComponent
from ..AccountComponent import AccountComponent
from ..HomeDetailsComponent import HomeDetailsComponent
from ..MedSuppliesComponent import MedSuppliesComponent
from ..AccomplishmentComponent import AccomplishmentComponent
from ..BotComponent import BotComponent
from anvil import *
from .. import data_access


home_form = None

def get_form():
  if home_form is None:
    raise Exception('You must set the Home Form First.')
  return home_form

def go_home():
    set_title("")
    set_activeNav('home')
    form = get_form()
    form.column_panelHome.clear()
  
    user = anvil.users.get_user()
    if user:
      form.load_cmpt(HomeDetailsComponent())
    else:
      form.load_cmpt(HomeAnonComponent())
pass
  
def go_request():
    set_title("Request")
    set_activeNav('request')
    
    user = require_account()
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return
      
    form = get_form()
    form.load_cmpt(RequestComponent())
pass
  
def go_records():
    set_title("Records")
    set_activeNav('records')
    form = get_form()

    user = require_account()
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return
      
      
    form.load_cmpt(AddMeasurementComponent())
pass
  
def go_inventory():
    set_title("Equipments")
    set_activeNav('inventory')
    form = get_form()
    user = require_account()
  
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return

    
    form.load_cmpt(InventoryComponent())
pass

def go_medsupplies():
    set_title("Med & Supplies")
    set_activeNav('medsupplies')
    form = get_form()
    user = require_account()
  
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return

    
    form.load_cmpt(MedSuppliesComponent())
pass

def go_accomplishment():
    set_title("Accomplishment")
    set_activeNav('accomplishment')
    form = get_form()
    user = require_account()
  
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return

    
    form.load_cmpt(AccomplishmentComponent())
pass

def go_account():
    set_activeNav('account')
    set_title("Account")
    form = get_form()
  
    user = require_account()
    if not user:
      Notification("Please Log in to use this feature").show()
      go_home()
      return
      
    form.load_cmpt(AccountComponent())
pass


def go_bot():
    set_activeNav('ask')
    set_title("Ask a Bot")

    '''user = require_account()
    if not user:
      go_home()
      return'''
    
      
    form = get_form()
    form.load_cmpt(BotComponent())
pass


def set_activeNav(state):
    form = get_form()
    form.set_activeNav(state)
pass

def set_title(text):
    form = get_form()
    baseTitle = form.baseTitle

    if text:
      form.labelTitle.text = baseTitle + ' - ' + text
    else:
      form.labelTitle.text = baseTitle
pass

def require_account():
  user = data_access.the_user()

  if user:
    return user

  user = anvil.users.login_with_form(allow_cancel=True)
  form = get_form()
  form.set_AccountState(user)
  return user


def refresh_window():
  anvil.js.window.location.reload(True)
  pass
  