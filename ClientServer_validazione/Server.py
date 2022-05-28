from email import message
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")



x = 0
while x < 3:
    message = socket.recv_string()
    if message == "porta":
        print("spedito alla porta")
        socket.send_string("8000")
        
    if message == 'due':
        socket.send_string("ti connetto")
        print(message)
    
    if message == 'uno':
        socket.send_string("aspetta")
        print(message)
    x += 1