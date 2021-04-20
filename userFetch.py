'''
    userFetch.py
    Fetch User Data From Database
'''
from session import session
from storage import teachers


def getUserInfo(sessKey, uid):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    node = teachers.globalTableTeachers[uid]
    """
        TODO : Database Support
        Fetch Database get info.
    """
    return node
