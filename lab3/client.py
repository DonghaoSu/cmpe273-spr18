import zmq
import sys
import threading

def sendToServer(username, send_msg_sock):
    
    while 1:
        msg = input("["+username+"] >")
        will_send = "["+ username +"] :" + msg
        send_msg_sock.send_string(will_send)
        send_msg_sock.recv()
   
def getFromServer(name, get_all_sock):  
    while 1:        
        all_from_sub = get_all_sock.recv()
        print("\n" + all_from_sub.decode('utf-8'))
    
def run():
    # ZeroMQ Context
    context = zmq.Context()

    #req/rep pattern setup
    send_msg_sock = context.socket(zmq.REQ)
    send_msg_sock.connect("tcp://127.0.0.1:5678")

    #pub/sub pattern setup
    get_all_sock = context.socket(zmq.SUB)
    get_all_sock.setsockopt(zmq.SUBSCRIBE, b"")
    get_all_sock.connect("tcp://127.0.0.1:5680")

    username = sys.argv[1]

    print("User["+ username+"] Connected to the chat server.")
    

    poller = zmq.Poller()
    # poller.register(send_msg_sock, zmq.POLLIN)
    poller.register(get_all_sock, zmq.POLLIN)

    # socks = dict(poller.poll())
    # for i in socks:
    #     print(socks[i])
    # socks = dict(poller.poll())
    # print(socks)

    while True:
        msg = input("["+username+"] >")
        will_send = "["+ username +"] :" + msg
        send_msg_sock.send_string(will_send)
        send_msg_sock.recv()

        keep_going = True
        
        while keep_going:
            socks = dict(poller.poll(50))
            if get_all_sock in socks and socks[get_all_sock] == 1:
                message = get_all_sock.recv()
                print(message.decode('utf-8'))
            else:
                keep_going = False

        
        # for send_msg_sock in socks:
        #     a = send_msg_sock.recv()

        # for get_all_sock in socks:
        #     message = get_all_sock.recv()
        #     print(message.decode('utf-8'))
        

    # t1 = threading.Thread(target=sendToServer, args=(username, send_msg_sock))
    # t2 = threading.Thread(target=getFromServer, args=('thread2', get_all_sock))
    # t1.start()
    # t2.start()
    
        
    
if __name__ == '__main__':
    run()
    