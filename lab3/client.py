import zmq
import sys

def send_message(name, message):
    data = {'username' : name,
            'message' : message}
    return data
def has_message(poller, display):
    events = poller.poll()
    return display in events
    #events = dict(poller.poll(3000))
    #return events.get(sock) == zmq.POLLIN


# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
display = context.socket(zmq.SUB)
display.setsockopt_string(zmq.SUBSCRIBE,'')
display.connect("tcp://127.0.0.1:5677")


sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")


#poller = zmq.Poller().register(sock, zmq.POLLIN)

msg = " ".join(sys.argv[1:])
print("user [{}] Connected to the chat server".format(msg))
name = msg
#sock.send_string(msg)
tit = "[{}] > ".format(name)

poller = zmq.Poller()
poller = poller.register(sock, zmq.POLLIN)


while 1:
    message = input(tit)
    data = send_message(name, message)
    sock.send_json(data)

    sock.recv_string()
    data = display.recv_json()
    username, message = data['username'], data['message']
    if(username != name):
        print("[{}]: {}".format(username, message))
