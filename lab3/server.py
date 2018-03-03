import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

display = context.socket(zmq.PUB)
display.bind("tcp://127.0.0.1:5677")


def get_message(sock):
    data = sock.recv_json()
    sock.send(b'\x00')
    username = data['username']
    message = data['message']
    return username,message

# Run a simple "Echo" server
while True:
    username, message = get_message(sock)
    data = {'username' : username,
            'message' : message}
    display.send_json(data)


    '''
    message = message.decode()
    message = message[::-1]
    sock.send_string("Echo: " + message)
    print("[Server] Echo: " + message)
    '''