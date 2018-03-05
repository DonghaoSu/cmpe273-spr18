import zmq
import sys
# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE, "1")
sock.connect("tcp://127.0.0.1:5680")

# while True:
#     message= sock.recv()
#     print message

username = sys.argv[1]

print("User[", username, "] Connected to the chat server.")

while True:
    msg = input("[",username,"] >")
    sock,send_string("[",username, "] :", msg)
    
    recvd = sock.recv().decode('utf-8')
    print(recvd)