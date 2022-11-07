import db_con#ssszZ
from flask import Flask,request
from flask_restful import Api ,Resource

app = Flask(__name__)
api = Api(app)

class create_account(Resource):
    def get(self):
        username = str(request.args["username"])
        password = str(request.args["password"])
        if username==None or password==None:
            return {"complete":False,
            "msg":"this api recive username and password as url paramiter"}
        db_con.create_account(username,password)
        return {"complete":True,"received":{"username":username,"password":password}}

class auth(Resource):
    def get(self):
        username = str(request.args["username"])
        password = str(request.args["password"])
        if (db_con.auth(username,password) == True):
            return {"complete":True,"received":{"username":username,"password":password}}
        else :
            return {"complete":False,"received":{"username":username,"password":password}}

class delete_account(Resource):
    def get(self):
        username = str(request.args["username"])
        password = str(request.args["password"])
        complete = db_con.delete_acount(username,password)
        return {"complete":complete,"receive":{"username":username,"password":password}}

## how to sent paramiter in python
# r = requests.get(url = URL, params = {'key':value})
##example ssszZ url : localhost/auth?username=something&?password=something

api.add_resource(create_account, '/create_account')
api.add_resource(auth, '/auth')
api.add_resource(delete_account,'/delete_account')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)