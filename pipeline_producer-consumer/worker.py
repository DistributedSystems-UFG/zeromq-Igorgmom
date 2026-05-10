import zmq, time, pickle, sys

PRODUCER_IP = sys.argv[1] if len(sys.argv) > 1 else "localhost"
WORKER_ID = sys.argv[2] if len(sys.argv) > 2 else "1"

def worker(id):
  context = zmq.Context()
  socket  = context.socket(zmq.PULL)
  socket.connect("tcp://" + PRODUCER_IP + ":12345")
  thisworker = format(int(id),'03d')

  while True:
    print("Worker " + thisworker + " wants work")
    work = pickle.loads(socket.recv())
    print("Worker " + thisworker + " gets   " + format(work,'03d'))
    time.sleep(work)

if __name__ == "__main__":
  worker(WORKER_ID)
