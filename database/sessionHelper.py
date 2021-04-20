"""
    session.py
    Access DB and retrive/add session keys
    @Author: Divakar Lakhera
    Todo: Add database support
"""
from session.sessionObjects import SessionBlock
"""
    def addSessionKey(key,uid) 
    returns: Boolean
    Adds Session key for the user in database
"""


def addSessionKey(key, uid) -> bool:
    # TODO: database support
    return True


"""
    def addSessionKey(sessionBlock)
    returns: Boolean
    Removes user Session Key from the database    
"""


def revokeSessionKey(sessionBlock) -> bool:
    # TODO: database support
    return True


"""
    def hasKey(key, uid)
    returns: Boolean
    Checks if a session key exists or not   
"""


def hasKey(key, uid) -> bool:
    # TODO: database support
    return True


"""
    def hasUser(uid)
    returns: Boolean
    Checks if user has a session key assigned or not 
"""


def hasUser(uid) -> SessionBlock:
    # TODO: database support
    return SessionBlock("ok", -1, "ok")


"""
    def authUser(user,passwd) -> bool:
    returns: uid of user (integer)
    Checks if user exist with provided username and password 
    Is UID is negative no user exists
"""


def authUser(user, passwd) -> int:
    # TODO: database support
    return 100
