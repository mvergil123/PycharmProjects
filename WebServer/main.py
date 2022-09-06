from flask import request
# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():

    file = open("index.html")
    return file.read()




@app.route('/bank')
def bank():
    file = open("bank.html")
    return file.read()

@app.route('/withdrawal')
def withdrawal():
    pass

@app.route('/deposit')
def deposit():
    with open("amount.txt", "a+") as handler:
        amount_text = handler.read()
        print("==============================")
        print(amount_text)

        amount = int(request.args.get('amount'))
        amount = amount_text + amount
        handler.write(str(amount))
        print(amount)
        return f"This is the amount ${amount}"

app.run()