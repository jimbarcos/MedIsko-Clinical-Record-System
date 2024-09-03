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
def passDate(value):
  anvil.server.session['date_value'] = value
@anvil.server.callable
def returnDate():
    return anvil.server.session.get('date_value', 'Default Value')

@anvil.server.callable
def passCampus(value):
  anvil.server.session['campus_value'] = value
@anvil.server.callable
def returnCampus():
    return anvil.server.session.get('campus_value', 'Default Value')

@anvil.server.callable
def passClinic(value):
  anvil.server.session['clinic_value'] = value
@anvil.server.callable
def returnClinic():
    return anvil.server.session.get('clinic_value', 'Default Value')


@anvil.server.callable
def passAuditDate(value):
  anvil.server.session['date_value'] = value
@anvil.server.callable
def returnAuditDate():
    return anvil.server.session.get('date_value', 'Default Value')

@anvil.server.callable
def passAuditPhysicianFirstName(value):
  anvil.server.session['physician_value2'] = value
@anvil.server.callable
def returnAuditPhysicianFirstName():
    return anvil.server.session.get('physician_value2', 'Default Value')

@anvil.server.callable
def passAuditPhysicianLastName(value):
  anvil.server.session['physician_value3'] = value
@anvil.server.callable
def returnAuditPhysicianLastName():
    return anvil.server.session.get('physician_value3', 'Default Value')
  
@anvil.server.callable
def passAuditUnit(value):
  anvil.server.session['unit_value'] = value
@anvil.server.callable
def returnAuditUnit():
    return anvil.server.session.get('unit_value', 'Default Value')

@anvil.server.callable
def passAuditPosition(value):
  anvil.server.session['position_value'] = value
@anvil.server.callable
def returnAuditPosition():
    return anvil.server.session.get('position_value', 'Default Value')





@anvil.server.callable
def passAccomplishmentDate(value):
  anvil.server.session['date_value'] = value
@anvil.server.callable
def returnAccomplishmentDate():
    return anvil.server.session.get('date_value', 'Default Value')

@anvil.server.callable
def passAccomplishmentPhysicianFirstName(value):
  anvil.server.session['physician_value'] = value
@anvil.server.callable
def returnAccomplishmentPhysicianFirstName():
    return anvil.server.session.get('physician_value', 'Default Value')

@anvil.server.callable
def passAccomplishmentPhysicianLastName(value):
  anvil.server.session['physician_value1'] = value
@anvil.server.callable
def returnAccomplishmentPhysicianLastName():
    return anvil.server.session.get('physician_value1', 'Default Value')

@anvil.server.callable
def passAccomplishmentUnit(value):
  anvil.server.session['unit_value'] = value
@anvil.server.callable
def returnAccomplishmentUnit():
    return anvil.server.session.get('unit_value', 'Default Value')

@anvil.server.callable
def passAccomplishmentPosition(value):
  anvil.server.session['position_value'] = value
@anvil.server.callable
def returnAccomplishmentPosition():
    return anvil.server.session.get('position_value', 'Default Value')