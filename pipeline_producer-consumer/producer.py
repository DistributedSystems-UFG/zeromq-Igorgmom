# pyrefly: ignore [missing-import]
import zmq, time, pickle, random

def producer():
  context = zmq.Context()              
  socket  = context.socket(zmq.PUSH)
  socket.bind("tcp://*:12345")
  
  while True:
    workload = random.randint(1, 100)
    print("Produced workload", format(workload,'03d'))
    socket.send(pickle.dumps(workload))
    time.sleep(workload/10)

if __name__ == "__main__":
  producer()
