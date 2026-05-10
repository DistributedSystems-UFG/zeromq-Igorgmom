# pyrefly: ignore [missing-import]
import zmq, time

def server():
  context = zmq.Context()         
  socket = context.socket(zmq.PUB)
  socket.bind("tcp://*:12345")
  while True:                    
    time.sleep(5)
    t = "TIME " + time.asctime()
    socket.send(t.encode())

if __name__ == "__main__":
  server()
