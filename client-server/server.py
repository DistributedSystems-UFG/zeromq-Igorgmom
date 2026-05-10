# pyrefly: ignore [missing-import]
import zmq

def server():
  context = zmq.Context()
  socket  = context.socket(zmq.REP)
  socket.bind("tcp://*:12345")

  while True:
    message = socket.recv()
    if not "STOP" in str(message):
      reply = str(message.decode())+'*'
      socket.send(reply.encode())
    else:                         
      break

if __name__ == "__main__":
  server()
