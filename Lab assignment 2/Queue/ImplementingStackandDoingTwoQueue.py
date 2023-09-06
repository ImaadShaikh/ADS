from QueueAssigmentMethod import *

class stackUsingQueue():
    def __init__(self):
        self.q1 = simpleQueue()
        self.q2 = simpleQueue()
    
    def NewPush(self,ele):
        return self.q1.enQueue(ele)
       
    
    def NewPop(self):
        while(self.q1.getCount() > 1):
            ele = self.q1.deQueue()
            self.q2.enQueue(ele)
        item = self.q1.deQueue

        while(self.q2.getCount() > 0):
            ele = self.q2.deQueue()
            self.q1.enQueue(ele) 
        return item
        
    def peekNew(self):
        while(self.q1.getCount()>1):
            self.q2.enQueue(self.q1.deQueue())
        ele=self.q1.QueuePeek()
        self.q2.enQueue(self.q1.deQueue())
        while(self.q2.getCount()>0):
            self.q1.enQueue(self.q2.deQueue())
        return ele
    
s1 = stackUsingQueue()
print(s1.NewPush(10))
print(s1.NewPush(20))
print(s1.NewPush(30))
print(s1.NewPush(40))
print(s1.NewPop())


