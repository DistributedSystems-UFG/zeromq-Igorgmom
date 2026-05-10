# pyrefly: ignore [missing-import]
import zmq
import sys

SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "localhost"

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)

  socket.connect("tcp://" + SERVER_IP + ":12345")
  socket.send(b"Hello world")
  message = socket.recv()
  socket.send(b"STOP")
  print(message.decode())

if __name__ == "__main__":
  client()
