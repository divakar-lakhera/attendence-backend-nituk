readme = """
<b> NIT UK - Grades Manager - Backend API <b><br>
---------------------------------------------<br><br>
<b> /session/verify/ </b> <br>
Accepts :  JSON Object POST Request  { 'user' : 'UserName' , 'pwd' : 'Password Hashed'} <br>
Returns :  JSON Object {"name": Current User Name, "uid": Unique User ID , "sessKey": SHA256 Session Key, "status": "ok"} <br>
Note : If authorisation fails, status will be set to "failed" and other keys may or may not be present. <br>
---------------------------------------------------------------------------------------------------------------------------------<br>

"""