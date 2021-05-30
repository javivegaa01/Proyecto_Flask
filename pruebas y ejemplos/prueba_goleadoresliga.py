#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

r_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
dic_competiciones=r_competiciones.json()
for info in dic_competiciones["data"]["competition"]:
    if info["name"]=="Premier League" and info["countries"][0]["name"]=="England":
        payload["competition_id"]=info["id"]
r_premier_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
dic_premier=r_premier_league.json()
for info in dic_premier["data"]["table"]:
    print(info["name"],info["team_id"])
payload.pop('competition_id','2')
print()
team1_id=input("Numero: ")
team2_id=input("Numero: ")
payload["team1_id"]=team1_id
payload["team2_id"]=team2_id
r_head2head=requests.get(URL_BASE+'teams/head2head.json',params=payload)
dic_head2head=r_head2head.json()
print('Fecha: '+dic_head2head["data"]["h2h"][0]["date"])
print('Local: '+dic_head2head["data"]["h2h"][0]["home_name"])
print('Visitante: '+dic_head2head["data"]["h2h"][0]["away_name"])
print('Resultado: '+dic_head2head["data"]["h2h"][0]["ft_score"])
    
#https://livescore-api.com/api-client/teams/head2head.json?team1_id=7&team2_id=19&key=WYJobu1gHeOCdKTI&secret=tiUk0AnaepL5ncNkawJm0KDIYrkcceVF
