#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET,'country':84}
#r=requests.get(URL_BASE+"countries/list.json",params=payload)
r1=requests.get(URL_BASE+"leagues/list.json",params=payload)
#doc=r.json()
doc1=r1.json()
#print(type(doc))

#for info in doc["data"]["country"]:
    #if info["name"]=="Champions League":
        #print(info)


#AFC,CAF,UEFA,CONMEBOL,FIFA

#print(doc1)
for info in doc1["data"]["league"]:
    print(info["id"])

#'https://livescore-api.com/api-client/scores/live.json?key=BvMEuAZzpZCSFZaJ&amp;secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH&amp;league=174'}
