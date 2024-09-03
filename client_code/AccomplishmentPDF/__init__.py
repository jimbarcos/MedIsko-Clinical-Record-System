from ._anvil_designer import AccomplishmentPDFTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from .. import data_access


class AccomplishmentPDF(AccomplishmentPDFTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.myAccomplishment = data_access.cacheAccomplishment()

    
    self.lblName.text = 'NAME: ' + str(anvil.server.call('returnAccomplishmentPhysicianFirstName')) + ' ' + str(anvil.server.call('returnAccomplishmentPhysicianLastName'))
    self.lblPosition.text = 'POSITION: ' + str(anvil.server.call('returnAccomplishmentPosition'))
    self.lblDateSubmission.text = 'DATE OF SUBMISSION: ' + str(anvil.server.call('returnAccomplishmentDate'))
    self.lblUnit.text = 'UNIT/DEPARTMENT: ' + str(anvil.server.call('returnAccomplishmentUnit'))
    
    self.repeating_panel_1.items = self.myAccomplishment.search(q.any_of(type="Respiratory Disorder"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_2.items = self.myAccomplishment.search(q.any_of(type="GI Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_3.items = self.myAccomplishment.search(q.any_of(type="Musc-Skeletal Dis."), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_4.items = self.myAccomplishment.search(q.any_of(type="BP Monitoring"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_5.items = self.myAccomplishment.search(q.any_of(type="Cardiovascular Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_6.items = self.myAccomplishment.search(q.any_of(type="CNS Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_7.items = self.myAccomplishment.search(q.any_of(type="Immune System Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_8.items = self.myAccomplishment.search(q.any_of(type="Derma Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_9.items = self.myAccomplishment.search(q.any_of(type="Surgery / Trauma"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_10.items = self.myAccomplishment.search(q.any_of(type="EENT Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_11.items = self.myAccomplishment.search(q.any_of(type="Reproductive Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_12.items = self.myAccomplishment.search(q.any_of(type="Nutritional Deficiency"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_13.items = self.myAccomplishment.search(q.any_of(type="Endocrine Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_14.items = self.myAccomplishment.search(q.any_of(type="Urinary Disorders"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_15.items = self.myAccomplishment.search(q.any_of(type="Medical Certificate"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_16.items = self.myAccomplishment.search(q.any_of(type="Injections"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_17.items = self.myAccomplishment.search(q.any_of(type="Ref. To Hospital W/O Nurse"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_18.items = self.myAccomplishment.search(q.any_of(type="Ref. To Hospital W/ Nurse"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_19.items = self.myAccomplishment.search(q.any_of(type="Referrals - Others"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_20.items = self.myAccomplishment.search(q.any_of(type="Consultation"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_21.items = self.myAccomplishment.search(q.any_of(type="Medical Clearance"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_22.items = self.myAccomplishment.search(q.any_of(type="On-Line Consultation - Others"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_23.items = self.myAccomplishment.search(q.any_of(type="Triage Survey"), tables.order_by('medicalservices', ascending = True))
    self.repeating_panel_24.items = self.myAccomplishment.search(q.any_of(type="Bulletin Updates"), tables.order_by('medicalservices', ascending = True))

    
    now = datetime.datetime.now()
    current_month = now.strftime("%B")
    current_year = now.year
    

    self.label_2.text = (
        'POLYTECHNIC UNIVERSITY OF THE PHILIPPINES\n'
        'Medical Services Department\n'
        'Sta. Mesa, Manila\n\n'
        'ACCOMPLISHMENT REPORT\n'
        f'As of {current_month} {current_year}\n'
    )

    recordstudent = self.myAccomplishment.search(tables.order_by('students', ascending=True))
    total_students = sum(record['students'] for record in recordstudent)
    self.txtallstudent.text = str(total_students)

    recordfaculty = self.myAccomplishment.search(tables.order_by('faculty', ascending=True))
    total_faculty = sum(record['faculty'] for record in recordfaculty)
    self.txtallfaculty.text = str(total_faculty)

    recordadmin = self.myAccomplishment.search(tables.order_by('admin', ascending=True))
    total_admin = sum(record['admin'] for record in recordadmin)
    self.txtalladmin.text = str(total_admin)

    recorddependents= self.myAccomplishment.search(tables.order_by('dependents', ascending=True))
    total_dependents = sum(record['dependents'] for record in recorddependents)
    self.txtalldependents.text = str(total_dependents)
    
    # Any code you write here will run before the form opens.
