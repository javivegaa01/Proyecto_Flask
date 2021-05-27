#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

r_info_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
dic_info_competiciones=r_info_competiciones.json()
lista_id_competiciones=[]
lista_nombre_competiciones=[]
for info in dic_info_competiciones["data"]["competition"]:
    if info["id"] not in lista_id_competiciones:
        lista_nombre_competiciones.append(info["name"])
        lista_id_competiciones.append(info["id"])

payload["competition_id"]=lista_id_competiciones[lista_nombre_competiciones.index("LaLiga Santander")]
r_info_goleadores=requests.get(URL_BASE+"competitions/goalscorers.json",params=payload)
dic_goleadores=r_info_goleadores.json()

for info in dic_goleadores["data"]["goalscorers"]:
    print(info["name"],info["team"]["name"])