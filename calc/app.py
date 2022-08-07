# Put your app in here.
from audioop import mul
from flask import Flask
from flask import request
from operations import *

app = Flask(__name__)

@app.route('/add', methods=["GET"])
def add_queryparams():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)


@app.route('/sub', methods=["GET"])
def sub_queryparams():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/mult', methods=["GET"])
def mult_queryparams():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b) 
    return str(result)

@app.route('/div', methods=["GET"])
def div_queryparams():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

"""further study"""
operations={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
@app.route('/math/<operation>')
def operation_based_on_input(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operation](a,b)

    return str(result)
