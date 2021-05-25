import os
import json
from lxml import etree
import requests
from flask import Flask, render_template,abort
app = Flask(__name__)

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}
doc_xml=etree.parse("fut.xml")


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
    lista_equipo=[]
    lista_ranking=[]
    lista_puntos=[]
    lista_dg=[]
    for grupos in lista_grupos:
        payload["group"]=grupos
        r_champions_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
        dic_champions_league=r_champions_league.json()
        lista=[]
        lista2=[]
        lista3=[]
        for info in dic_champions_league["data"]["table"]:
            lista.append(info["name"])
            lista2.append(info["points"])
            lista3.append(info["goal_diff"])
            if info["rank"] not in lista_ranking:
                lista_ranking.append(info["rank"])
        lista_equipo.append(lista)
        lista_puntos.append(lista2)
        lista_dg.append(lista3)
    return render_template("champions.html",lista_grupos=lista_grupos,lista_ranking=lista_ranking,lista_equipo=lista_equipo,lista_puntos=lista_puntos,lista_dg=lista_dg)

@app.route('/clasificacion',methods=["GET"])
def clasificacion():
    nombres= doc_xml.xpath("//clasificacion/team/name/text()")
    puntos= doc_xml.xpath("//clasificacion/team/points/text()")
    goles_marcados=doc_xml.xpath("//clasificacion/team/goals_scored/text()")
    goles_encajados=doc_xml.xpath("//clasificacion/team/goals_conceded/text()")
    diferencia_de_goles=[]
    for elem1,elem2 in zip(goles_marcados,goles_encajados):
        a=int(elem1)-int(elem2)
        diferencia_de_goles.append(str(a))
    return render_template("clasificacion.html",lista_nombres=nombres,lista_puntos=puntos,lista_goles=diferencia_de_goles)

#port=os.environ["PORT"]
#'0.0.0.0',int(port)
app.run(debug=True)