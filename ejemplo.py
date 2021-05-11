#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
r=requests.get(URL_BASE+"matches/stats.json?match_id=172252&key="+KEY+"&secret="+SECRET)
doc=r.json()

print(type(doc))

print(doc)


#(URL_BASE"matches/stats.json?match_id=172252&key="+KEY+"&secret="+SECRET)

#match_id=172252&