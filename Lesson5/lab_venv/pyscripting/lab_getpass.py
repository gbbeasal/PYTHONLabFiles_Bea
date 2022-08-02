import requests
from getpass import getpass

creds = requests.get('https://api.github.com/user', auth=('gbbeasal',getpass()))

print(creds)