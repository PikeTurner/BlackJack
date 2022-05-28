
import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")



x = 0
while x < 3:
    message = socket.recv_string()
    #message = json.loads(message)
    print(message)
    if message['azione'] == 'connetti':
        print('conneso')
    x += 1