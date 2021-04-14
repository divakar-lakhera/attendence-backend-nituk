from flask import Flask
from flask import jsonify, request
from session import session
import intro
from json import JSONEncoder
import json
from flask_cors import CORS
import userFetch
from subjectAPI import *

app = Flask(__name__)
CORS(app)


class encoderJSON(JSONEncoder):
    def default(self, o):
        return o.__dict__


def convertToJSON(block):
    returnBlock = encoderJSON().encode(block)
    returnBlock = json.loads(returnBlock)
    return returnBlock


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


@app.route('/user/', methods=['POST'])
def getUserInfo():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    returnBlock = userFetch.getUserInfo(sessKey, userId)
    returnBlock = encoderJSON().encode(returnBlock)
    returnBlock = json.loads(returnBlock)
    return jsonify(returnBlock)


@app.route('/subject/fetch/', methods=['POST'])
def getSubList():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    returnBlock = getSubject(sessKey, userId, subId)
    return jsonify(convertToJSON(returnBlock))


@app.route('/subject/addStudent/', methods=['POST'])
def addStudent():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    stdId = rawData['studentId']
    return jsonify(
        convertToJSON(
            addStudentToSubject(
                sessKey,
                userId,
                subId,
                stdId
            )
        )
    )


@app.route('/subject/removeStudent/', methods=['POST'])
def removeStudent():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    stdId = rawData['studentId']
    return jsonify(
        convertToJSON(
            removeStudentToSubject(
                sessKey,
                userId,
                subId,
                stdId
            )
        )
    )


@app.route('/subject/auditAdd/', methods=['POST'])
def addAudit():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    stdId = rawData['studentId']
    return jsonify(
        convertToJSON(
            addStudentToAudit(
                sessKey,
                userId,
                subId,
                stdId
            )
        )
    )


@app.route('/subject/auditRemove/', methods=['POST'])
def removeAudit():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    stdId = rawData['studentId']
    return jsonify(
        convertToJSON(
            removeStudentFromAudit(
                sessKey,
                userId,
                subId,
                stdId
            )
        )
    )


@app.route('/subject/update/', methods=['POST'])
def updatePacket():
    rawData = request.get_json()
    sessKey = rawData['sessKey']
    userId = rawData['uid']
    subId = rawData['subjectId']
    return jsonify(
        convertToJSON(
            updateSubjectBlock(
                sessKey,
                userId,
                subId,
                rawData
            )
        )
    )
