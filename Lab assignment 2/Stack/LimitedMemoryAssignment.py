class simplestack:
    def __init__(self):
        self.Defaultsize = 5
        self.count = 0
        self.data = [None]*self.Defaultsize
        self.front = -1 
    
    def getCount(self):
        return self.count 
    def isStackEmpty(self):
        return self.count == 0
    def isStackFull(self):
        return self.count == len(self.data)
    def StackPush(self,ele):
        if not self.isStackFull() :
            self.front += 1
            self.data[self.front] = ele
            self.count += 1  
            return self.count 
        else:
            return None
    def StackPop(self):
        if not self.isStackEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return None 
    def StackPeek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return None
    def printelement(self):
        for i in range(-1,0):
            return self.data