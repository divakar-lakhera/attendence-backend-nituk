"""
    session.py
    Manage and Authenticate Session/Requests via API
    @Author: Divakar Lakhera
    Todo: Add database support
"""
from database import sessionHelper
import hashlib
import time

MAGIC_SALT = "93C632F6915879116741159447529D54BCACB84FC97EE6FFCE2A9296E4ED039F"


class SessionBlock:
    def __init__(self, name, uid, sessKey):
        self.name = name
        self.uid = uid
        self.sessKey = sessKey


def authUser(name, passwd) -> bool:
    return sessionHelper.authUser(name, passwd)


def createSession(name, uid) -> SessionBlock:
    # Check if user already exist
    if sessionHelper.hasUser(uid):
        return SessionBlock(None, None, None)
    # build new hash for user
    newRawString = str(time.time()) + name + str(uid) + MAGIC_SALT
    newHash = hashlib.sha256(newRawString).hexdigest()
    sessionHelper.addSessionKey(str(newHash), uid)
    return SessionBlock(name, uid, newHash);


def isValidSession(sessKey, uid) -> bool:
    return sessionHelper.hasKey(sessKey, uid)


def revokeSession(sessKey, uid) -> bool:
    if not sessionHelper.hasKey(sessKey, uid):
        return False
    return sessionHelper.revokeSessionKey(sessKey, uid)
