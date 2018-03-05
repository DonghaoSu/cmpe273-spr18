import time
import grpc
import ping_pb2
import ping_pb2_grpc
import sys
import re
from concurrent import futures

class PingServer(ping_pb2_grpc.PingPongServicer):
    
    def __init__(self, start_coor, dist):
        self.start_coor = start_coor
        self.dist = dist
        self.count = 0
        self.location_map = {}

    def ping(self, request, context):
        request_id = request.id
        if request_id in self.location_map:
            return ping_pb2.Response(loc=stringToIntList(self.location_map[request_id]), id=request_id)
        else:
            self.location_map[request_id] = None
            print("Client id [", request_id, "] is not registered yet!")
# a           b           c
# "0,0,0" + "10,0,0" = "10,0,0"

# c = sum(map(int, a.split(",")), map(int, b.split(",")))
    def update(self, request, context):
        request_id = request.id
        
        while True:
            updated_loc = str(stringToIntList(self.start_coor)[0] + stringToIntList(self.dist)[0]*request_id)+","+str(stringToIntList(self.start_coor)[1] + stringToIntList(self.dist)[1]*request_id)+"," + str(stringToIntList(self.start_coor)[2] + stringToIntList(self.dist)[2]*request_id)
            output = map(int, updated_loc.split(','))
            yield ping_pb2.Response(loc=output, id=request_id)
        
    def register(self, request, context):
        request_id = request.id
        if request_id == -1:
            cur_count = self.count
            self.count += 1
            if cur_count == 0:
                self.location_map[0] = self.start_coor
            else:
                self.location_map[cur_count] = str(stringToIntList(self.location_map[cur_count-1])[0] + stringToIntList(self.dist)[0])+","+str(stringToIntList(
                    self.start_coor)[1] + stringToIntList(self.dist)[1])+"," + str(stringToIntList(self.start_coor)[2] + stringToIntList(self.dist)[2])
            return ping_pb2.Response(loc=stringToIntList(self.location_map[cur_count]), id=cur_count)
        else:
            if request_id in self.location_map:
                print("This ID already exist.")
            

def stringToIntList(newPos):
    new_loc_string_list = newPos.split(',')
    x = int(new_loc_string_list[0])
    y = int(new_loc_string_list[1])
    z = int(new_loc_string_list[2])
    return [x ,y, z]

def run(host, port):
    start_coor = sys.argv[1]
    dist = sys.argv[2]
    ping_server = PingServer(start_coor, dist)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    ping_pb2_grpc.add_PingPongServicer_to_server(ping_server, server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    
    try:
        print("Server started at...%d" % port)
        while True:
            newPos = input("Enter New Cooridnate[x, y, z]:")
            if re.match("[0-9]+,[0-9]+,[0-9]+",newPos) != None:
                ping_server.location_map[0] = newPos
                ping_server.start_coor = newPos
            else:
                print("Please enter a coordinate like the following format: 1,2,3")
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run('0.0.0.0', 3000)
