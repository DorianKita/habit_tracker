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

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)