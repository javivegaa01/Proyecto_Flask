#Enunciado:
#Este programa será un administrador de información sobre la champions league, en el cúal podrás consultar los partidos. 

#Librerias necesarias
import requests
import json
import os
from tabulate import tabulate
#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

##Lista competiciones
r_competiciones=requests.get(URL_BASE+"countries/list.json",params=payload)
dic_competiciones=r_competiciones.json()
for info in dic_competiciones["data"]["country"]:
    if info["name"]=="Champions League":
        cad=info["leagues"]
        payload["country"]=cad[-2:]
r_champions_league=requests.get(URL_BASE+"leagues/list.json",params=payload)
dic_grupos_champions_league=r_champions_league.json()
lista_grupos=[]
for info in dic_grupos_champions_league["data"]["league"]:
    if info["name"].startswith("Gr"):
        lista_grupos.append(info["name"][-1:])
        payload.pop('country',84)

##Información competiciones
r_info_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
dic_info_competiciones=r_info_competiciones.json()
for info in dic_info_competiciones["data"]["competition"]:
    if info["name"]=="Champions League" and info["federations"][0]["name"]=="UEFA":
        payload["competition_id"]=info["id"]


#for grupos in lista_grupos:
payload["group"]="A"
r_champions_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
dic_champions_league=r_champions_league.json()
datos=[]
for info in dic_champions_league["data"]["table"]:
    lista=[]
    lista=[info["rank"],info["name"],info["points"],info["goal_diff"]]
    datos.append(lista)
titulo=["GRUPO A",""]
print(tabulate(titulo,headers='firstrow',tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))
print(tabulate(datos,headers=['Puesto','Equipo','Puntos','Goal Average'],tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))

    



#https://livescore-api.com/api-client/leagues/table.json?key=BvMEuAZzpZCSFZaJ&secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH&competition_id=244&group=A

#https://livescore-api.com/api-client/competitions/list.json?key=BvMEuAZzpZCSFZaJ&secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH

