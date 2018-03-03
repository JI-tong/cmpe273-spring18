from __future__ import print_function
import grpc
import drone_pb2_grpc
import sys
from drone_pb2 import Request#, StartDancerResult,PeerDancerResult

class CoClient():
    def __init__(self, host = '0.0.0.0', port = 3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = drone_pb2_grpc.CoordinateStub(self.channel)

    def get(self, id):
        response = self.stub.get(Request(id = int(id)))
        for i in response:
            print("[received] moving to [{},{},{}]".format(i.dancer.x, i.dancer.y, i.dancer.z))

        return

    def setup(self):
        return self.stub.setup(Request())


def test():
    client = CoClient()
    resp = client.setup()
    print("Client id [{}] connected to the server".format(resp.id))
    client.get(resp.id)

if __name__ == '__main__':
    test()
