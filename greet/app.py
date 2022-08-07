from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/welcome', methods=["GET"])
def welcome_msg():
    return "welcome"

@app.route('/welcome/home', methods=["GET"])
def welcome_home():
    return "welcome home"

@app.route('/welcome/back', methods=["GET"])
def welcome_back():
    return "welcome back"