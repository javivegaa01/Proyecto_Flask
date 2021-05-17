#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}
r=requests.get(URL_BASE+"countries/list.json",params=payload)
doc=r.json()

print(type(doc))

for info in doc["data"]["country"]:
    if info["name"]=="Champions League":
        print(info)
    #if info["is_real"]=="0":
        #print(info["name"])
    #if type(info["national_team"])!="dict":
        #print(info["name"])

#AFC,CAF,UEFA,CONMEBOL,FIFA

