# pyrefly: ignore [missing-import]
import zmq
import sys
import time

SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "localhost"

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)
  socket.connect("tcp://" + SERVER_IP + ":12345")
  socket.setsockopt(zmq.SUBSCRIBE, b"TIME")

  for i in range(5):
    time = socket.recv()
    print(time.decode())

if __name__ == "__main__":
  client()
