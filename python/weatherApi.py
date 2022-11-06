import json
import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=39.103119&lon=-84.512016&appid=a4c7631f6fb70fa741aa39fe41704ce7')

data = r.json()
print(data)
