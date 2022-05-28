import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000")

message = socket.recv_string()
print(message)
socket.send_string("approvato")