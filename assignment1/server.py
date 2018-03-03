import time
import grpc
import drone_pb2
import drone_pb2_grpc
import sys
import threading
#from drone_pb2 import Request

from concurrent import futures

class CoServer(drone_pb2_grpc.CoordinateServicer):
    def __init__(self):
        self.init = sys.argv[1].split(",")
        self.dis = sys.argv[2].split(",")
        self.id = 0
        self.map = {}
        self.lock = threading.Lock()

    def setup(self, request, context):
        self.id += 1
        return drone_pb2.RegistResult(id = self.id)



    def get(self, request, context):
        # TODO
        id = request.id
        if(id == 1):
            while 1 :
                start = self.init
                dancer = drone_pb2.Dancer(x = int(start[0]),
                y = int(start[1]), z = int(start[2]))
                self.map[id] = dancer
                yield drone_pb2.PeerDancerResult(dancer = dancer)
                self.init = input("Enter New Coordinate[x,y,z] > ").split(",")

        else:
            while 1:
                x = self.map[id - 1].x + int(self.dis[0])
                y = self.map[id - 1].y + int(self.dis[1])
                z = self.map[id - 1].z + int(self.dis[2])
                dancer = drone_pb2.Dancer(x = x, y = y, z = z)
                self.map[id] = dancer
                old = self.map[id - 1]
                yield drone_pb2.PeerDancerResult(dancer = dancer)
                while(self.map[id - 1] == old):
                    continue



def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drone_pb2_grpc.add_CoordinateServicer_to_server(CoServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)