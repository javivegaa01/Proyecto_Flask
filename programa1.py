#Enunciado:
#Este programa será un administrador de información sobre la champions league, en el cúal podrás consultar los partidos. 

#Librerias necesarias
import requests
import json
import os
from info_programa_1 import *

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

payload["competition_id"]=f_id_competicion
for a in f_lista_grupos:
    payload["group"]=a
    r_champions_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
    dic_champions_league=r_champions_league.json()
    payload.pop["group",a]
    print(dic_champions_league)



     
#https://livescore-api.com/api-client/leagues/table.json?key=BvMEuAZzpZCSFZaJ&secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH&competition_id=244&group=A

#https://livescore-api.com/api-client/competitions/list.json?key=BvMEuAZzpZCSFZaJ&secret=xmgkAwKEopD0wXa8tWMYxMxWMaPr9ZbH

