import zmq
import sys


def send_message(name, message):
    data = {'username' : name,
            'message' : message}
    return data



# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
display = context.socket(zmq.SUB)
display.setsockopt_string(zmq.SUBSCRIBE,'')
display.connect("tcp://127.0.0.1:5677")


sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")


receiver = context.instance().socket(zmq.PAIR)
sender = context.instance().socket(zmq.PAIR)



poller = zmq.Poller()  
poller.register(sock, zmq.POLLIN)  

poller2 = zmq.Poller()
poller2.register(display, zmq.POLLIN)

msg = " ".join(sys.argv[1:])
print("user [{}] Connected to the chat server".format(msg))
name = msg
#sock.send_string(msg)
tit = "[{}] > ".format(name)


while 1:
    msg = dict(poller2.poll(1000))
    while(msg.get(display) == zmq.POLLIN):
        #print("has something")
        data = display.recv_json()
        username, message = data['username'], data['message']
        if(username != name):
            print("[{}]: {}".format(username, message))
        msg = dict(poller2.poll(1000))

    #sender.send_string("[{}]: {}".format(username, message))
    #message = receiver.recv_string()
    #events = dict(poller.poll())
    #if(events.get(sock) == zmq.POLLIN):
    #    sock.recv()
    #    print(message)
    message = input(tit)
    if(message != ''):
        data = send_message(name, message)
        sock.send_json(data)
        sock.recv()

'''
my-venv) ton9ericdeMacBook-Air:lab3 ton9eric$ python3 client.py Bob
user [Bob] Connected to the chat server
[Bob] >
[Alice]: Hi from Alice
[Bob] > Hello world
[Bob] >
[Alice]: Good to see you Bob!
[Bob] > Yeah, I'm glad to see you!
[Bob] > Hope you have a nice day!
[Bob] > Nice to meet you!
[Bob] >
[Alice]: Me too!

(my-venv) ton9ericdeMacBook-Air:lab3 ton9eric$ python3 client.py Alice
user [Alice] Connected to the chat server
[Alice] > Hi from Alice
[Alice] >
[Bob]: Hello world
[Alice] > Good to see you Bob!
[Alice] >
[Bob]: Yeah, I'm glad to see you!
[Bob]: Hope you have a nice day!
[Bob]: Nice to meet you!
[Alice] > Me too!
[Alice] >

'''