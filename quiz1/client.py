from ping_pb2 import Request, Response
import grpc
import ping_pb2_grpc

class PingClient():
    def __init__(self, host = '0.0.0.0', port = 3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host,port))
        self.stub = ping_pb2_grpc.PingPongStub(self.channel)

    def ping(self, data):
        req = Request(data = str(data))
        return self.stub.pong(req)

def test():
    client = PingClient()
    resp = client.ping("ping")
    print("Request = {}".format(resp.data))

if __name__ == '__main__':
    test()
