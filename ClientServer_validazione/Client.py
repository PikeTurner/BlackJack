from threading import Thread
import zmq
import socket
import json

context = zmq.Context()
sc = context.socket(zmq.REQ)
sc.connect("tcp://localhost:5555")

ctx = {
    'azione': 'connetti',
    'mess': socket.gethostbyname(socket.gethostname()),
}

ctx = json.dumps(ctx)
sc.send_string('ctx')
'''
message = sc.recv_string()
print(message)

socket.send_string("porta")
porta = socket.recv_string()
'''
def connessioneServer(porta):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:" + porta)
    
    socket.send_string("connesso alla porta 8000")
    message = socket.recv_string()
    print(message)

    t = Thread(target=connessioneServer, args=(porta,))
    t.start()