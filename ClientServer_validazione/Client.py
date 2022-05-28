from threading import Thread
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send_string("due")
message = socket.recv_string()
print(message)

socket.send_string("porta")
porta = socket.recv_string()

def connessioneServer(porta):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:" + porta)
    
    socket.send_string("connesso alla porta 8000")
    message = socket.recv_string()
    print(message)

t = Thread(target=connessioneServer, args=(porta,))
t.start()