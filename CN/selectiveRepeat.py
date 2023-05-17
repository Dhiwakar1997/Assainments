import time

WINDOW_SIZE = 3 
TIMEOUT = 2

def send(packet):
    print("Sending packet:", packet)
    time.sleep(1)
    return True 
def receive():
    print("Waiting for packet...")
    time.sleep(1) 
    return True 

def selective_repeat(data):
    base = 0
    next_seq_num = 0
    sent_packets = []
    while base < len(data):
        for i in range(WINDOW_SIZE):
            if next_seq_num < len(data):
                packet = data[next_seq_num]
                send(packet)
                sent_packets.append(packet)
                next_seq_num += 1
        try:
            ack_packet = receive()
            if ack_packet in sent_packets:
                sent_packets.remove(ack_packet)
                if ack_packet == data[base]:
                    base += 1
        except TimeoutError:
            print("Timeout expired. Resending packets...")
            next_seq_num = base
            sent_packets = []

data = ["packet1", "packet2", "packet3", "packet4", "packet5"]
selective_repeat(data)
