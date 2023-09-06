from QueueAssigmentMethod import *

class stackUsingQueue():
    def __init__(self):
        self.q1 = simpleQueue()
    
    def NewPush(self,ele):
        self.q1.enQueue(ele)
        return self.q1.getCount
    
    def NewPop(self):
        c = self.q1.getCount
        while(c > 1):
            self.q1.enQueue(self.q1.deQueue())
            c -= 1 
            ele = self.q1.deQueue()
        while(c > 1):
            self.q1.enQueue(self.q1.deQueue()) 
            c -= 1 
            return ele
        
    def peekNew(self):
        c = self.q1.getCount
        while(c>1):
            self.q1.enQueue(self.q1.deQueue())
            c -=1
        ele=self.q1.QueuePeek()
        self.q1.enQueue(self.q1.deQueue())
        while(c>1):
            self.q1.enQueue(self.q1.deQueue())
            c -=1
        return ele
    
s1=stackUsingQueue()
s1.NewPush(10)
assert(s1.NewPush()==10)
s1.NewPush(20)
s1.NewPush(30)
s1.NewPush(50)
assert(s1.NewPop()==50)
assert(s1.NewPop()==50)
assert(s1.NewPop()==30)
assert(s1.peekNew()==20)
