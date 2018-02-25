from flask import Flask
from flask import request
from flask import Response
app = Flask(__name__)

@app.route("/")
def hello():
    # name = request.form["name"]
    return "Hello World!"


map = {}
user_id = '1'
@app.route('/users', methods = ['POST'])
def user():
    """modify/update the information for <user_id>"""

    name = request.form["name"]
    map[user_id] = name
    #return "POST, id = {}, name = {}\n".format(user_id, name)
    #print "POST, id = {}, name = {}\n".format(user_id, name)
    return Response("POST, id = {}, name = {}\n".format(user_id, name), status = 201)

@app.route('/users/<user_id>', methods = ['GET','DELETE'])
def getname(user_id):
    #user_id = request.get["user_id"]
    if(request.method == 'GET'):
        return "GET, id = {}, name = {}\n".format(user_id, map[user_id])
    else:
        map[user_id] = ''
        return Response(status = 204)
