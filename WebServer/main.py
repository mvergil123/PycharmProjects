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
    amount_text = int(output.read())
    return amount_text


def save_amount_in_bank(amount):
    print(amount)
    os.system(f'echo "1${amount}" > amount.txt')


@app.route('/deposit')
def deposit():
    # update the amount
    amount = int(request.args.get('amount'))
    amt = get_amount_in_bank() + amount
    print(amt)
    save_amount_in_bank(amt)
    return "We have deposited your money!"

app.run()