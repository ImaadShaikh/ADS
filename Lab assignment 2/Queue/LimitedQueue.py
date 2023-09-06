class simplestack:
    def __init__(self):
        self.DefaultSize = 5
        self.data = [None]*self.DefaultSize
        self.count = 0
        self.front = -1

    def getCount(self):
        return self.count
    
    def isStackEmpty(self):
        return self.count == 0
    
    def isStackFull(self):
        return self.count == len(self.data)
    
    def enQueue(self,ele):
        if not self.isStackFull():
            self.front += 1
            self.data[self.front]=ele
            self.count += 1 
        else:
            return None
    
    def deQueue(self):
        if not self.isStackEmpty():
            self.count -=1
            return self.data.pop(0)
        else:
            return None
    
    def StackPeek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return None
    
    def PrintElements(self):
        return self.data