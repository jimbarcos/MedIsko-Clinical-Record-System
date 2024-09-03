from ._anvil_designer import HomeDetailsComponentTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from .. import data_access
from .. import navigation
import anvil.js


class HomeDetailsComponent(HomeDetailsComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.records = data_access.recordDisp()
    for i in self.records:
      self.label_1.text = self.label_1.text + "\n{} {} {} {} {} {}\n".format(i['RecordDate'], i['Name'], i['Age'], i['Weight'], i['Sex'], i['AssignedStaff'])
      #print("{} {} {}".format(i['RecordDate'], i['Name'], i['Age']))
    # Any code you write here will run before the form opens.
   
    user = data_access.the_user()
    self.lblHello.text = 'Account: ' + str(user['email'])

    # self.set_graph()
    # self.load_data()
  
  def set_graph(self):
    self.outlined_cardNoData.visible = False #len(self.records) == 0
    self.outlined_cardData.visible = False #len(self.records) > 0

    self.plot_records.layout.xaxis.title = 'Day'
    self.plot_records.layout.xaxis.showgrid = True
    self.plot_records.layout.xaxis.zeroline = True
    self.plot_records.layout.xaxis.showline = True
    self.plot_records.layout.xaxis.mirror = 'ticks'
    self.plot_records.layout.xaxis.gridcolor = '#bdbdbd'
    self.plot_records.layout.xaxis.gridwidth = 2
    self.plot_records.layout.xaxis.zerolinecolor = '#969696'
    self.plot_records.layout.xaxis.zerolinewidth = 4
    self.plot_records.layout.xaxis.linecolor = '#636363'
    self.plot_records.layout.xaxis.linewidth = 6
    
    self.plot_records.layout.yaxis.title = 'Age and Weight'
    self.plot_records.layout.yaxis.showgrid = True
    self.plot_records.layout.yaxis.zeroline = True
    self.plot_records.layout.yaxis.showline = True
    self.plot_records.layout.yaxis.mirror = 'ticks'
    self.plot_records.layout.yaxis.gridcolor = '#bdbdbd'
    self.plot_records.layout.yaxis.gridwidth = 2
    self.plot_records.layout.yaxis.zerolinecolor = '#969696'
    self.plot_records.layout.yaxis.zerolinewidth = 4
    self.plot_records.layout.yaxis.linecolor = '#636363'
    self.plot_records.layout.yaxis.linewidth = 6


  def load_data(self):
    self.records = data_access.recordDisp()

    if not self.records:
      return

    #x
    day = [] 
    #y
    age = []
    weight = []

    for idx, m in enumerate(self.records):
      day.append(m['RecordDate'])
      age.append(m['Age'])
      weight.append(m['Weight'])

    self.plot_records.data = [
      go.Scatter(
        x = day,
        y = age,
        name = "Age of Patients"
      ), go.Bar(
        x = day,
        y = weight,
        name = "Weight of Patients"
      )
    ]
    pass
    
  def outlined_button_1_click(self, **event_args):
    navigation.go_records()
    
    pass

