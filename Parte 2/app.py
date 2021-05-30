import os
import json
from lxml import etree
import requests
from flask import Flask, render_template,abort,request
app = Flask(__name__)

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}
doc_xml=etree.parse("fut.xml")


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

          
@app.route('/champions',methods=["GET","POST"])
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

@app.route('/clasificacion',methods=["GET","POST"])
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

@app.route('/clasificacion/<equipo>',methods=["GET"])
def gol(equipo):
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
        if info["team"]["name"]==equipo:
            return render_template("goleador.html",jugador=info["name"],goles=info["goals"],equipo=equipo)

@app.route('/premier',methods=["GET","POST"])
def premier():
    r_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
    dic_competiciones=r_competiciones.json()
    for info in dic_competiciones["data"]["competition"]:
        if info["name"]=="Premier League" and info["countries"][0]["name"]=="England":
            payload["competition_id"]=info["id"]
    r_premier_league=requests.get(URL_BASE+'leagues/table.json',params=payload)
    dic_premier=r_premier_league.json()
    lista_equipos=[]
    for info in dic_premier["data"]["table"]:
        lista_equipos.append(info["name"]+" --> "+info["team_id"])
    if request.method == "GET":
        return render_template("premier.html",lista_equipos=lista_equipos)
    else:
        payload["team1_id"]=request.form.get("team1_id")
        payload["team2_id"]=request.form.get("team2_id")
        r_head2head=requests.get(URL_BASE+'teams/head2head.json',params=payload)
        dic_head2head=r_head2head.json()
        lista=[dic_head2head["data"]["h2h"][0]["date"],dic_head2head["data"]["h2h"][0]["home_name"],dic_head2head["data"]["h2h"][0]["away_name"],dic_head2head["data"]["h2h"][0]["ft_score"]]
        return render_template("premier.html",lista=lista,lista_equipos=lista_equipos)
port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)