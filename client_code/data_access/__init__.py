import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import navigation


__records = []
__cacheIventory = []
__cacheIventoryHistory = []
__cacheMedicine = []
__cacheSupplies = []
__cacheRequestHistory = []
__cacheAudit = []
__cacheIventoryAudit = []
__cacheAccomplishment = []
__cacheInventoryAccomplishment = []
__user = None

def recordDisp():
  global __records
  if __records:
    return __records

  __records = list(anvil.server.call('record_disp'))
  return __records


def addRecord(record_date, name, age, weight, sex, assignedStaff):
  global __records
  __records = []
  
  return anvil.server.call('add_record', record_date, name, age, weight, sex, assignedStaff)

def the_user():
  global __user

  if __user:
    return __user

  __user = anvil.users.get_user()
  return __user


def logout ():
  global __user
  __user = None

def cacheInventory():
  global __cacheIventory
  if __cacheIventory:
    return __cacheIventory

  __cacheIventory = anvil.server.call('displayInventory')
  return __cacheIventory

def cacheInventoryHistory():
  global __cacheIventoryHistory
  if __cacheIventoryHistory:
    return __cacheIventoryHistory

  __cacheIventoryHistory = anvil.server.call('displayInventoryHistory')
  return __cacheIventoryHistory

def cacheRequestHistory():
  global __cacheRequestHistory
  if __cacheRequestHistory:
    return __cacheRequestHistory

  __cacheRequestHistory = anvil.server.call('displayRequestHistory')
  return __cacheRequestHistory

def cacheRequestMedicine():
  global __cacheMedicine
  if __cacheMedicine:
    return __cacheMedicine

  __cacheMedicine = anvil.server.call('displayRequestMedicine')
  return __cacheMedicine

def cacheRequestSupplies():
  global __cacheSupplies
  if __cacheSupplies:
    return __cacheSupplies

  __cacheSupplies = anvil.server.call('displayRequestSupplies')
  return __cacheSupplies


def cacheAudit():
  global __cacheAudit
  if __cacheAudit:
    return __cacheAudit

  __cacheAudit = anvil.server.call('displayAudit')
  return __cacheAudit

def cacheInventoryAudit():
  global __cacheIventoryAudit
  if __cacheIventoryAudit:
    return __cacheIventoryAudit

  __cacheIventoryAudit = anvil.server.call('displayInventoryAudit')
  return __cacheIventoryAudit


def cacheAccomplishment():
  global __cacheAccomplishment
  if __cacheAccomplishment:
    return __cacheAccomplishment

  __cacheAccomplishment = anvil.server.call('displayAccomplishment')
  return __cacheAccomplishment

def cacheInventoryAccomplishment():
  global __cacheInventoryAccomplishment
  if __cacheInventoryAccomplishment:
    return __cacheInventoryAccomplishment

  __cacheInventoryAccomplishment = anvil.server.call('displayInventoryAccomplishment')
  return __cacheInventoryAccomplishment