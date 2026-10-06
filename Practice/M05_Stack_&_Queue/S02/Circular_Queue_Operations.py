'''
size = 5 
li = [None] * size 
print(li)
'''


class Circular_Queue:
    def __init__(self,size):
        self.queue = [None] * self.size 
        self.front = -1 
        selfrear = -1
        
    def enqueue(self, value):
        #check if queue is full
        if (self.real + 1)