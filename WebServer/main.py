from flask import request
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
    search = request.args.get("search")
    page = request.args.get("page")
    print(search)
    print(page)
    return 'test'


app.run()