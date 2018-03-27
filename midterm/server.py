from flask import Flask


from flask import Flask
from flask import request
from flask import Response

import collections

app = Flask(__name__)
MAX_LEN=3

@app.route('/')
def index():
    return 'OK'


deque = collections.deque(maxlen = 3)
# TODO add all routes here!
@app.route('/items', methods = ['POST'])
def item():
    name = request.form["name"]
    deque.append(name)
    #return "POST, id = {}, name = {}\n".format(user_id, name)
    #print "POST, id = {}, name = {}\n".format(user_id, name)
    return Response(status = 201)

@app.route('/items', methods = ['GET'])
def getname():
    #user_id = request.get["user_id"]
    #for i in deque:
    #    print("{},".format(i))
    out = ""
    for i in list(deque):
        out += i
        out += ","
    out = out[: -1]
    return Response("{}\n".format(out), status = 200)

@app.route('/items/<index>', methods = ['GET'])
def getindex(index):
    #user_id = request.get["user_id"]
    

    return Response("{}\n".format(deque[int(index)]), status = 200)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)