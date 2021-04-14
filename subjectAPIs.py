from session import session


def getSubject(sessKey, uid, subjectID):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    # check for auth to fetch !
    # TODO : Add Layer of Auth
    # TODO : Fetch from DATABASE (Pending)
    node = {
        "numRows": 3,
        "row_1": ['Roll Number', 'Name', 'Mid Term 1', 'Mid Term 2'],
        "row_2": ['BT18CSE032', 'Random Name 1', 43, 43],
        "row_3": ['BT18CSE042', 'Random Name 2', 54, 12]
    }
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
    dataRows = packet['dataBlock']['numRows']
    for i in range(1, dataRows + 1):
        idx = "row_" + str(i)
        print(packet['dataBlock'][idx])
    # TODO : Add Database Support
    return {'status': 'ok'}
