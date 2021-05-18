import requests
import json
import os
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

def f_lista_grupos():
    r_competiciones=requests.get(URL_BASE+"countries/list.json",params=payload)
    dic_competiciones=r_competiciones.json()
    for info in dic_competiciones["data"]["country"]:
        if info["name"]=="Champions League":
            cad=info["leagues"]
            payload["country"]=cad[-2:]
    r_champions_league=requests.get(URL_BASE+"leagues/list.json",params=payload)
    dic_champions_leage=r_champions_league.json()
    lista_grupos=[]
    for info in dic_champions_leage["data"]["league"]:
        if info["name"].startswith("Gr"):
            lista_grupos.append(info["name"][-1:])
            payload.pop('country',84)
    return lista_grupos


def f_id_competicion():
    r_info_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
    dic_info_competiciones=r_info_competiciones.json()
    for info in dic_info_competiciones["data"]["competition"]:
        if info["name"]=="Champions League" and info["federations"][0]["name"]=="UEFA":
            id_competicion=info["id"]
    return id_competicion




