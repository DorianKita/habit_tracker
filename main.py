import dotenv
import requests
from dotenv import load_dotenv
import os

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

graph_endpoint = 'https://pixe.la/v1/users/dolan/graphs'

response = requests.post(url=graph_endpoint, json=graph_config)
