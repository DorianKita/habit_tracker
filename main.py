import requests
from charset_normalizer.api import explain_handler
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'
API_KEY = os.environ.get('TOKEN')

user_params = {
    'token': API_KEY,
    'username': 'dolan',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    'id': 'graph1',
    'name': 'Cycling',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': API_KEY
}

graph_endpoint = 'https://pixe.la/v1/users/dolan/graphs'

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now = datetime.now()
formatted_date = now.strftime('%Y%m%d')

pixel_config = {
    'date': formatted_date,
    'quantity': '1',
}

pixel_endpoint = 'https://pixe.la/v1/users/dolan/graphs/graph1'

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

