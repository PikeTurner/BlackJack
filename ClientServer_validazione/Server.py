
import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")



x = 0
while x < 3:
    
    message = json.loads(socket.recv_json())
    print(message)
    if message['azione'] == 'connetti':
        socket.send_string('8000')
    x += 1