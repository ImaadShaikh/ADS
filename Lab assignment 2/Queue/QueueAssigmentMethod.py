class simpleQueue:
    def __init__(self):
        self.data = []
        self.count = 0
    def getCount(self):
        return self.count
    def isQueueEmpty(self):
        return self.count == 0
    def enQueue(self,ele):
        self.data.append(ele)
        self.count = self.count +1
        return self.count
    def deQueue(self):
        if not self.isQueueEmpty():
            self.count -=1
            return self.data.pop(0)
        else:
            return None
    def QueuePeek(self):
        if not self.isQueueEmpty():
            return self.data[-1]
        else:
            return None
    def PrintElements(self):
        for i in range(-1,0):
            return self.data
        
