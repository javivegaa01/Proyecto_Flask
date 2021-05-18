#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

r_lista_paises=requests.get(URL_BASE+"countries/list.json",params=payload)
dic_lista_paises=r_lista_paises.json()

for info in dic_lista_paises["data"]["country"]:
    if info["is_real"]=="1" and info["name"]=="Argentina":
        payload["country"]=info["leagues"][-2:]
r_ligas=requests.get(URL_BASE+"leagues/list.json",params=payload)
dic=r_ligas.json()
for info in dic["data"]["league"]:
    print(info["name"],info["scores"])
        

#http://livescore-api.com/api-client/leagues/list.json?key=BvMEuAZzpZCSFZaJ&secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH&country=65
