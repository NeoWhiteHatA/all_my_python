import time
import random


class Que:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
def enq(self, item):
    self.items.insert(0, item)

def dq(self):
    return self.items.pop()

def size(self):
    return len(self.items)
    
    def  simulate_line(self, till_show, max_time):
        pq = Que()
        tix_sold = []
        
        for i in range(10):
            pq.enq('movie-fanat' + str(i))
    
    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dq()
        print(person)
        tix_sold.append(person)
return tix_sold