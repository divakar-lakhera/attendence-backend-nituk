"""
    session.py
    Manage and Authenticate Session/Requests via API
    @Author: Divakar Lakhera
    Todo: Add database support
"""
from database import sessionHelper
import hashlib
import time
from session.sessionObjects import SessionBlock

MAGIC_SALT = "93C632F6915879116741159447529D54BCACB84FC97EE6FFCE2A9296E4ED039F"




def authUser(name, passwd) -> int:
    uid = sessionHelper.authUser(name, passwd)
    return uid


def createSession(name, uid) -> SessionBlock:
    # Check if user already exist
    tmp = sessionHelper.hasUser(uid)
    if tmp.uid > 0:
        return tmp
    # build new hash for user
    newRawString = str(time.time()) + name + str(uid) + MAGIC_SALT
    newHash = hashlib.sha256(newRawString.encode('utf-8')).hexdigest()
    sessionHelper.addSessionKey(str(newHash), uid)
    return SessionBlock(name, uid, newHash);


def isValidSession(sessKey, uid) -> bool:
    return sessionHelper.hasKey(sessKey, uid)


def revokeSession(sessKey, uid) -> bool:
    if not sessionHelper.hasKey(sessKey, uid):
        return False
    return sessionHelper.revokeSessionKey(sessKey, uid)
