#Enunciado:
#Muestra los grupos de la Champions Leage 19/20

#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

#Programa
r_competiciones=requests.get(URL_BASE+"countries/list.json",params=payload)
dic_competiciones=r_competiciones.json()
for info in dic_competiciones["data"]["country"]:
    if info["name"]=="Champions League":
        cad=info["leagues"]
        payload["country"]=cad[-2:]

r_champions_league=requests.get(URL_BASE+"leagues/list.json",params=payload)
dic_champions_leage=r_champions_league.json()
for info in dic_champions_leage["data"]["league"]:
    if info["name"]=="Gr":
        del payload[country]
        cad=info["scores"]
        payload["leagues"]=cad[-2:]


scores/live.json
        




