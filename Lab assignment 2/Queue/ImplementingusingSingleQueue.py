from QueueAssigmentMethod import *

class UsingSingleQueue():
    def __init__(self):
        self.q1 = simpleQueue()

    def NewPush(self,ele):
        return self.q1.enQueue(ele)
    
    def NewPop(self):
        while(self.q1.getCount()>1):
            self.q1.enQueue(self.q1.deQueue())
            self.q1.count-=1
        return self.q1.deQueue()
    
s1 = UsingSingleQueue()
print(s1.NewPush(10))
print(s1.NewPush(20))
print(s1.NewPush(30))
print(s1.NewPop())
