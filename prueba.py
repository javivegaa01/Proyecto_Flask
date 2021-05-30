import os
import json
from lxml import etree
import requests
from flask import Flask, render_template,abort
app = Flask(__name__)

#Declaración de variables
URL_BASE="https://soccer.sportmonks.com/api/v2.0/"
API_TOKEN=os.environ["api_token"]
#G4VwesavWS8jqZv9DSYd9Ewc4PmA3qz6D6fad2ncR3opTrm5wnM81DB3ZEIU
payload={'api_token':API_TOKEN}
r_ligas=requests.get(URL_BASE+"leagues",params=payload)
dic_ligas=r_ligas.json()
print(dic_ligas)
for info in dic_ligas["data"]:
    print(info["name"])

#https://soccer.sportmonks.com/api/v2.0/leagues?api_token={API_TOKEN}