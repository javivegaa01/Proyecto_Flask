#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

#Información de los países
r_lista_paises=requests.get(URL_BASE+"countries/list.json",params=payload)
dic_lista_paises=r_lista_paises.json()

#PROGRAMA
print()
print("Bienvenido al programa")
print()
continuar=input("¿Quieres comenzar a ver las ligas de cada país? (s/n)" )
while continuar=="s":
    if continuar=="n":
        break
    for info in dic_lista_paises["data"]["country"]:
        lista=[]
        pais=info["name"]
        if info["is_real"]=="1" and pais==info["name"]:
            cad=info["leagues"].split("country=")
            payload["country"]=cad[1]
            r_lista_ligas=requests.get(URL_BASE+"leagues/list.json",params=payload)
            dic_lista_ligas=r_lista_ligas.json()
            for info in dic_lista_ligas["data"]["league"]:
                lista.append(info["name"])
            print()
            eleccion=input("¿Quieres ver las ligas que hay en %s ? (s/n) " % pais)
            if eleccion=="s":
                if len(lista)!=0:
                    print()
                    print(pais)
                    print("-------Ligas---------")
                    for elem in lista:
                        print(elem)
                else:
                    print("Lo siento, no hay datos sobre %s" % pais)
            payload.pop('country',cad[1])
    continuar=input("¿Continuas? (s/n)")

print()
print("Fin del programa")

