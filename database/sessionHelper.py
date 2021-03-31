"""
    session.py
    Access DB and retrive/add session keys
    @Author: Divakar Lakhera
    Todo: Add database support
"""

"""
    def addSessionKey(key,uid) 
    returns: Boolean
    Adds Session key for the user in database
"""


def addSessionKey(key, uid) -> bool:
    # TODO: database support
    return True


"""
    def addSessionKey(key,uid)
    returns: Boolean
    Removes user Session Key from the database    
"""


def revokeSessionKey(key, uid) -> bool:
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


def hasUser(uid) -> bool:
    # TODO: database support
    return True


"""
    def authUser(user,passwd) -> bool:
    returns: Boolean
    Checks if user exist with provided username and password 
"""


def authUser(user, passwd) -> bool:
    # TODO: database support
    return True
