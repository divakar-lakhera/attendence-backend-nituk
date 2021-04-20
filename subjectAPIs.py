from session import session
from storage import subjects


def getSubject(sessKey, uid, subjectID):
    # check for auth to fetch !
    # TODO : Add Layer of Auth
    # TODO : Fetch from DATABASE (Pending)
    node = subjects.globalsTableSubjects[subjectID]
    return node


def addStudentToSubject(sessKey, uid, subjectID, studentID):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # TODO : Get Database Support
    # Add row to database
    return {'status': 'ok'}


def removeStudentToSubject(sessKey, uid, subjectID, studentID):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # TODO : Get Database Support
    # Add row to database
    return {'status': 'ok'}


def addStudentToAudit(sessKey, uid, subjectID, studentID):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # TODO : Get Database Support
    # Add row to database
    return {'status': 'ok'}


def removeStudentFromAudit(sessKey, uid, subjectID, studentID):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # TODO : Get Database Support
    # Add row to database
    return {'status': 'ok'}


def updateSubjectBlock(sessKey, uid, subjectID, packet):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # Start Update on database
    # Use Subject ID to select table
    datablock = packet['data']
    for i in datablock:
        for j in range(7):
            try:
                subjects.globalsTableSubjects[subjectID]['data'][i]['marks'][j] = datablock[i][j]
            except KeyError:
                continue
    # TODO : Add Database Support
    return {'status': 'ok'}
