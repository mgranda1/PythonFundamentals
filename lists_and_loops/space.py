# Retrieving data from API using requests module
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print("People in space and their spacecraft:")
for person in json['people']:
    print(person['name'], person['craft'])