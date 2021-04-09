'''
    userFetch.py
    Fetch User Data From Database
'''
from session import session


def getUserInfo(sessKey, uid):
    if not session.isValidSession(sessKey, uid):
        return {"status": "failed"}
    node = {"status": "ok",
            "name": "dummy",
            "userType": 0,
            "subs": ["subject1", "subject2", "subject3"]
            }
    """
        TODO : Database Support
        Fetch Database get info.
    """
    return node
