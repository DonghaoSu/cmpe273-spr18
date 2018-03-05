from ping_pb2 import Request, Response
import grpc
import ping_pb2_grpc
import time
import sys

class Drone():
    def __init__(self, host='0.0.0.0', port=3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host,port))
        self.stub = ping_pb2_grpc.PingPongStub(self.channel)
        resp = self.stub.register(Request(id=-1))
        self.id = resp.id
        
    def ping(self):
        return self.stub.ping(Request(id=self.id))

def test():
    input_port = sys.argv[1]

    client = Drone()
    print("Client id[", client.id, "] connected to the server.")
    resp = client.ping()  
    print("[received] moving to", resp.loc)
    last_loc = resp.loc

    try:
        while True: 
            for response in client.stub.update(Request(id=client.id)):  
                if response.loc != last_loc:
                    print("[received] now moving to", response.loc)
                    last_loc = response.loc         
            time.sleep(0.1)
    except KeyboardInterrupt:
        client.stop(0)
    
if __name__ == '__main__':
    test()
