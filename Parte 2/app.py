import os
import json
import requests
from flask import Flask, render_template,abort
from tabulate import tabulate
app = Flask(__name__)

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}



@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

          
@app.route('/champions',methods=["GET"])
def champions_league():
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
    for grupos in lista_grupos:
        payload["group"]=grupos
        r_champions_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
        dic_champions_league=r_champions_league.json()
        datos=[]
        for info in dic_champions_league["data"]["table"]:
            lista=[]
            lista=[info["rank"],info["name"],info["points"],info["goal_diff"]]
            datos.append(lista)
    return render_template("champions.html",datos=datos)
#port=os.environ["PORT"]
#'0.0.0.0',int(port)
app.run(debug=True)