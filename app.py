from flask import Flask
from flask import jsonify, request
from session import session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "/session/verify/ : send POST request ({ 'user' : 'username','pwd' : 'passwordHash'}) to the URL to check " \
           "if user exists /n returns { 'status' : 'ok'} "


# Session API Start

@app.route('/session/verify/', methods=['POST'])
def authLogin():
    rawData = request.get_json()
    userName = rawData['user']
    paswd = rawData['pwd']
    session.authUser(userName, paswd)
    retCode = {'status':'ok'}
    return jsonify(retCode)

"""
curl --header "Content-Type: application/json"  --request POST  --data '{"user":"someUser","pwd:"secret"}' http://127.0.0.1:5000//session/verify
"""