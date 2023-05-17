import time

def send(packet):
    print("Sending packet:", packet)
    time.sleep(1) # simulate transmission delay
    return True # assume packet was successfully transmitted

def receive():
    print("Waiting for packet...")
    time.sleep(1) # simulate propagation delay
    return True # assume packet was successfully received

def stop_and_wait(data):
    for i in range(len(data)):
        packet = data[i]
        ack_received = False
        while not ack_received:
            ack_received = send(packet) and receive()
            if not ack_received:
                print("Timeout expired. Resending packet:", packet)

data = ["packet1", "packet2", "packet3", "packet4", "packet5"]
stop_and_wait(data)
