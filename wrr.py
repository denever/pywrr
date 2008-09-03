from random import randint
import sys

class Packet:
    def __init__(self, pkt_id, size):
        self.id = pkt_id
        self.size = size

    def get_id(self):
        return self.id
    
    def get_size(self):
        return self.size

class WRRQueue:
    def __init__(self, weights, avg_pkt_size):
        self.weights = weights
        self.avg_pkt_size = avg_pkt_size
        
        weight = weights[0]

        for i, w in enumerate(self.weights):
            if w < weight:
                weight = w
                
        self.min_weight = weight
        
    def next_pkt_size_in_cid(self, i):
        pkt_to_send = self.weights[i] / self.min_weight
        return pkt_to_send * self.avg_pkt_size
    
if __name__ == '__main__':
    queues = []
    pkt_id = 0
    
    for i in range(0,4):
        packets = []
        for j in range(0,100):
            packet = Packet(pkt_id, randint(20,400))
            packets.append(packet)
        queues.append(packets)

    requests = []
    
    for cid, queue in enumerate(queues):
        cid_byte_size = 0

        for pkt in queue:
            cid_byte_size = cid_byte_size + pkt.get_size()

        requests.append(cid_byte_size)
        
    for cid, size in enumerate(requests):
        print 'Cid: %d has %d bytes' % (cid, size)

    weights = []

    for i in range(0,4):
        weights.append(randint(1,12))
        print 'Cid: %d has weight %d' % (i, weights[i])

    wrr = WRRQueue(weights, 180)
        

    for cid,queue in enumerate(queues):
        pkt_size = wrr.next_pkt_size_in_cid(cid)
        while(pkt_size > 0):
            print 'Dequeue from cid %d of a pkt with size %d' % (cid,pkt_size)
            pkt_pos = 0
        
            for pos, pkt in enumerate(queue):
                if pkt.get_size() <= pkt_size:
                    pkt = queue.pop(pkt_pos)
                    pkt_size = pkt_size - pkt.get_size()
                    print 'Dequeue pkt at pos: %d, pkt size: %d' % (pkt_pos, pkt.get_size())
                    break
                print pkt_size
