import os
import json
from flask import Flask, render_template,abort,request
app = Flask(__name__)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

#port=os.environ["PORT"]
#'0.0.0.0',int(port)
app.run(debug=True)