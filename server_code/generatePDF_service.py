import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.pdf

@anvil.server.callable
def create_pdf():
    pdf = anvil.pdf.render_form('InventoryPDF')
    return pdf

@anvil.server.callable
def create_pdfRequest():
    pdf = anvil.pdf.render_form('RequestPDF')
    return pdf

@anvil.server.callable
def create_pdfAudit():
    pdf = anvil.pdf.render_form('MedSuppliesPDF')
    return pdf

@anvil.server.callable
def create_pdfAccomplishment():
    pdf = anvil.pdf.render_form('AccomplishmentPDF')
    return pdf
