import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
# msg = " ".join(sys.argv[1:])
# print("[Client]:" + msg)
# sock.send_string(msg)

# print(sock.recv().decode('utf-8'))

username = sys.argv[1]

print("User["+ username+"] Connected to the chat server.")

while 1:
    msg = input("["+username+"] >")
    will_send = "["+ username +"] :" + msg
    sock.send_string(will_send)
    recvd = sock.recv().decode('utf-8')
    print(recvd)
    # while recvd != None:
    #         print(recvd)