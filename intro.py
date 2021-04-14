readme = """
<b> NIT UK - Grades Manager - Backend API </b> <br>
---------------------------------------------<br><br>
<b> /session/verify/ </b> <br>
Accepts :  JSON Object POST Request  { 'user' : 'UserName' , 'pwd' : 'Password Hashed'} <br>
Returns :  JSON Object {"name": Current User Name, "uid": Unique User ID , "sessKey": SHA256 Session Key, "status": "ok"} <br>
Note : If authorisation fails, status will be set to "failed" and other keys may or may not be present. <br>
---------------------------------------------------------------------------------------------------------------------------------<br>
<br>
<br>
<b> /user/ </b><br>
Accepts : JSON Object POST Request { 'sessKey' : SHA256 Session Key , 'uid' : User ID } <br>
Returns : JSON Object { 'name' : Current User Name, "
<br>
<br>
---------------------------------------------<br>
<b> Subject API </b><br>
---------------------------------------------
<br>
<br>
<b> /subject/fetch/ </b> <br>
Accepts : JSON Object POST Request { "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" } <br>
Returns : JSON Object Format --  <br>
&emsp;{<br>
&emsp;&emsp;            "numRows": 3,<br>
&emsp;  &emsp;          "row_1": ['Roll Number', 'Name', 'Mid Term 1', 'Mid Term 2'],<br>
&emsp; &emsp;           "row_2": ['BT18CSE032', 'Random Name 1', 43, 43],<br>
&emsp; &emsp;           "row_3": ['BT18CSE042', 'Random Name 2', 54, 12]<br>
 &emsp;   }<br>
<br>
<b> /subject/addStudent/ </b><br>
Adds Student to a specific student. <br>
Accepts : JSON Object POST Request {  "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" , "studentID":" BT18CSE002" } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br>
<b> /subject/removeStudent/ </b><br>
Removes Student to a specific student. <br>
Accepts : JSON Object POST Request {  "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" , "studentID":" BT18CSE002" } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br>
<b> /subject/removeStudent/ </b><br>
Removes Student to a specific student. <br>
Accepts : JSON Object POST Request {  "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" , "studentID":" BT18CSE002" } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br>
<b> /subject/auditAdd/ </b><br>
Adds Student to audit list in that subject <br>
Accepts : JSON Object POST Request {  "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" , "studentID":" BT18CSE002" } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br>
<b> /subject/auditRemove/ </b><br>
Removes Student from the audit list in that subject  <br>
Accepts : JSON Object POST Request {  "sessKey": SHA256 Session Key , "uid": userID , "subjectId": "CSL012" , "studentID":" BT18CSE002" } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br> 
<b> /subject/update/ </b><br>
Updates the whole table with new data <br>
Accepts : JSON Object POST Request...Format <br>
&emsp;&emsp;{   "sessKey": SHA256 Session Key , <br>
&emsp;&emsp;&emsp;    "uid": userID , <br>
&emsp;&emsp;&emsp;    "subjectId": "CSL012" , <br>
&emsp;&emsp;&emsp;    "dataBlock": { <br>
&emsp;&emsp;&emsp;&emsp;"numRows" : Number of rows to update (Warning wrong number might cause DB commit errors), <br>
&emsp;&emsp;&emsp;&emsp;"row_1": [ <br>
&emsp;&emsp;&emsp;&emsp;&emsp;"BT18CSE001", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            "Random Name 1", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            23, (new marks here)<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;            31 (new marks here , set 0 if not applied)<br>
 &emsp;&emsp;&emsp;       ],<br>
&emsp;&emsp;&emsp;&emsp;        "row_2": [ <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            "BT18CSE032", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            "Random Name 2", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            43, <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            43 <br>
  &emsp;&emsp;&emsp;        ], <br>
&emsp;&emsp;&emsp;&emsp;         "row_3": [ <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            "BT18CSE042", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            "Random Name 3", <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            54, <br>
&emsp;&emsp;&emsp;&emsp;&emsp;            12 <br>
 &emsp;&emsp;&emsp;         ] <br>
 &emsp;&emsp;    }  <br>
 &emsp; } <br>
Returns : JSON Object { "status" : "ok" } or fail <br>
<br> 
"""