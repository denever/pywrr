from random import randint

if __name__ == '__main__':
    queues = []
    weights = []

    for i in range(0,4):
        size = randint(20, 1000)
        queues.append(size)
    
    for i in range(0,4):
        weight = randint(1, 13)
        weights.append(weight)
    
    # find smallest weight
    min_weight = 13

    for i in weights:
        if i < min_weight:
            min_weight = i
    
    print 'Min weight:', min_weight

#    bytes_res = 0
    avg_pkt_size = 100
    for i,queue in enumerate(queues):
        byte_re = avg_pkt_size * int(weights[i] / min_weight)
        print byte_re


        
        
