from ._anvil_designer import MedSuppliesPDFTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import data_access
from .. import navigation
import datetime

class MedSuppliesPDF(MedSuppliesPDFTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAudit = data_access.cacheAudit()

    self.label_2_copy_3.text = 'NAME: ' + str(anvil.server.call('returnAuditPhysicianFirstName')) + ' ' + str(anvil.server.call('returnAuditPhysicianLastName'))
    self.label_2_copy_3_copy.text = 'POSITION: ' + str(anvil.server.call('returnAuditPosition'))
    self.label_2_copy_3_copy_2.text = 'DATE OF SUBMISSION: ' + str(anvil.server.call('returnAuditDate'))
    self.label_2_copy_3_copy_copy.text = 'UNIT/DEPARTMENT: ' + str(anvil.server.call('returnAuditUnit'))
    
    self.repeating_panel_1.items = self.myAudit.search(q.any_of(type="ANALGESIC"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_2.items = self.myAudit.search(q.any_of(type="MUSCLE RELAXANT"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_3.items = self.myAudit.search(q.any_of(type="ANTIPYRETICS"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_4.items = self.myAudit.search(q.any_of(type="MUCOLYTIC"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_5.items = self.myAudit.search(q.any_of(type="DECONGESTANT"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_6.items = self.myAudit.search(q.any_of(type="ANTITUSSIVE"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_7.items = self.myAudit.search(q.any_of(type="ANTI – HYPERTENSION"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_8.items = self.myAudit.search(q.any_of(type="CORONARY DILATOR"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_9.items = self.myAudit.search(q.any_of(type="ANTIVERTIGO"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_10.items = self.myAudit.search(q.any_of(type="ANTIBIOTIC"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_11.items = self.myAudit.search(q.any_of(type="ANTISPASMODIC"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_12.items = self.myAudit.search(q.any_of(type="GASTROKINETIC/ANTIEMETIC"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_13.items = self.myAudit.search(q.any_of(type="ANTIMOTILITY"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_14.items = self.myAudit.search(q.any_of(type="ELECTROLYTE ORAL"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_15.items = self.myAudit.search(q.any_of(type="ANTACID/ANTIFLATULENT"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_16.items = self.myAudit.search(q.any_of(type="PROTON PUMP INHIBITOR"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_17.items = self.myAudit.search(q.any_of(type="ANTIHISTAMINE"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_18.items = self.myAudit.search(q.any_of(type="ANTI – ASTHMA"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_19.items = self.myAudit.search(q.any_of(type="TOPICAL OINTMENT"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_20.items = self.myAudit.search(q.any_of(type="EYE / EAR DROPS"), tables.order_by('medicineMaterial', ascending = True))
    self.repeating_panel_21.items = self.myAudit.search(q.any_of(type="SUPPLIES"), tables.order_by('medicineMaterial', ascending = True))
    
    
    now = datetime.datetime.now()
    current_month = now.strftime("%B")
    current_year = now.year
    

    self.label_2.text = (
        'POLYTECHNIC UNIVERSITY OF THE PHILIPPINES\n'
        'Medical Services Department\n'
        'Sta. Mesa, Manila\n\n'
        'INVENTORY OF MEDICINES AND SUPPLIES\n'
        f'As of {current_month} {current_year}\n'
    )


    

    # Any code you write here will run before the form opens.
