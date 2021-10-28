import requests

BASE = 'http://localhost:5000/'
response = requests.get(BASE + 'helloWorld')
print(response.json())