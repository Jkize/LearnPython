# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:54:14 2019

@author: Jhoan Saavedra
"""

from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

#app.run(host='0.0.0.0',port=14); Para que lo puedan leer desde otros dispositivos

@app.route('/foro',methods=['POST','GET'])
def f2():
    A=request.json
    print(A)
    B=A['num']
    return str(B*2)

app.run(host='0.0.0.0',port=14) #Siempre va al final