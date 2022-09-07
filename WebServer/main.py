from flask import request
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():

    file = open("index.html")
    content = file.read()
    file.close()
    return content

@app.route('/bank')
def bank():
    file = open("bank.html")
    content = file.read()
    file.close()
    return content

@app.route('/withdrawal')
def withdrawal():
    pass


def get_amount_in_bank():
    output = os.popen('cat amount.txt')
    amount_text = float(output.read())
    return amount_text


def save_amount_in_bank(amount):
    file = open('amount.txt', 'w+')
    file.write(str(amount))
    file.close()


@app.route('/deposit')
def deposit():
    # update the amount
    amount = float(request.args.get('amount'))
    amt = get_amount_in_bank()
    total = amt + amount
    save_amount_in_bank(total)
    return "We have deposited your money!"

app.run()