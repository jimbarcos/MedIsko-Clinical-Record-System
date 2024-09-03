import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import uuid
import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

@anvil.server.http_endpoint('/authorize')
def authorize():
  data = anvil.server.request.body_json

  if not data:
    return anvil.server.HttpResponse(400, 'You must submit a JSON body via POST')

  email = data.get('email')
  password = data.get('password')

  if not email or not password:
    return anvil.server.HttpResponse(403, 'Email and Password are required')

  try:
    user = anvil.users.login_with_email(email, password)
    if not user:
      return anvil.server.HttpResponse(403, 'Invalid login')
  except anvil.users.AuthenticationFailed:
    return anvil.server.HttpResponse(403, 'Invalid login')

  api_key_mode = 'existing'
  
  if not user ['api_key']:
    user['api_key'] = str(uuid.uuid4())
    api_key_mode = 'created'
  return {'api_key' : user['api_key'], 'mode' : api_key_mode}
    
  return {'key' : 'Reached the line end return statement'}

@anvil.server.http_endpoint('/add_record')
def add_record ():
  data = anvil.server.request.body_json
  user, error = login_request(data)




  if error:
    return error

  age = int(data.get('age', 0))
  weight = int(data.get('weight', 0))
   

  recorded_date_str = data.get('recorded')
  if recorded_date_str is not None:
      recorded_date = datetime.datetime.strptime(recorded_date_str, '%Y-%m-%d').date()
      # Convert the recorded date to a string
      data['recorded'] = recorded_date.isoformat()
      recorded = data['recorded']
  
  app_tables.addrecords.add_row(CreatedDate=datetime.datetime.now(), 
                                RecordDate= recorded_date, 
                                Age=age, 
                                Weight=weight, 
                                User=user)
              
  
  return {
    "status": "success"
  }
  pass

def login_request (data):
  if not data:
    return None, anvil.server.HttpResponse(400, 'You must submit a JSON body via POST')

  try:
    email = data.get('email')
    api_key = data.get('api_key')

    if not email or not api_key:
      return None, anvil.server.HttpResponse(403, 'Email and API key are required')

    user = app_tables.users.get(email=email)
    if not user or not api_key or not user['api_key'] == api_key:
      return None, anvil.server.HttpResponse(403, 'Invalid login')

    return user, None
  except Exception as x:
    return None, anvil.server.HttpResponse(403, 'Invalid Login: {}'.format(x))


    

@anvil.server.http_endpoint('/hello/:name')
def hello(name, **query_params):
  return {
    'message' : 'Hello {} from the API'.format(name),
    'body' : anvil.server.request.body_json,
    'query' : query_params
  }

@anvil.server.route('/generateHi')
def hi():
  return {
    'message' : 'Hi from the API'
  }
