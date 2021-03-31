from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Boiz"

