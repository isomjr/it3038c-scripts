import json
import requests

r = requests.get("http://127.0.0.1:3000/")

data = r.json()
counter = 0
for key in data:
    info = data[counter]['name'] + " is " + data[counter]['color']
    print(info)
    counter+=1

