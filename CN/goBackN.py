import time

WINDOW_SIZE = 3 # number of packets that can be sent at a time
TIMEOUT = 2 # in seconds

def send(packet):
    print("Sending packet:", packet)
    time.sleep(1) # simulate transmission delay
    return True # assume packet was successfully transmitted

def receive():
    print("Waiting for packet...")
    time.sleep(1) # simulate propagation delay
    return True # assume packet was successfully received

def go_back_n(data):
    base = 0
    next_seq_num = 0
    while base < len(data):
        # send packets within the window
        for i in range(WINDOW_SIZE):
            if next_seq_num < len(data):
                packet = data[next_seq_num]
                send(packet)
                next_seq_num += 1
        # wait for acknowledgements
        try:
            ack_received = receive()
            if not ack_received:
                print("Timeout expired. Resending packets...")
                next_seq_num = base
        except TimeoutError:
            print("Timeout expired. Resending packets...")
            next_seq_num = base

data = ["packet1", "packet2", "packet3", "packet4", "packet5"]
go_back_n(data)