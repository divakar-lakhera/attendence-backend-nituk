from flask import Flask
from flask import jsonify, request
from session import session
import intro
from json import JSONEncoder
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class encoderJSON(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route('/')
def hello_world():
    return intro.readme


# Session API Start
@app.route('/session/verify/', methods=['POST'])
def authLogin():
    rawData = request.get_json()
    userName = rawData['user']
    paswd = rawData['pwd']
    uid = session.authUser(userName, paswd)
    if uid < 0:
        return jsonify({'status': 'failed'})
    userBlock = session.createSession(userName, uid)
    userBlock = encoderJSON().encode(userBlock)
    xblock = json.loads(userBlock)

    xblock.update({'status': 'ok'})
    return json.dumps(xblock)
