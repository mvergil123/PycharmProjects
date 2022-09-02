
# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():

    file = open("start.html")
    return file.read()




# @app.route('/bank')
# def bank():
#     file = open("bank.html")
#     return file.read()

app.run()