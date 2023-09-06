class simplestack:
    def __init__(self):
        self.data = []
        self.count = 0
    def getCount(self):
        return self.count
    def isStackEmpty(self):
        return self.count ==0
    def StackPush(self,ele):
        self.data.append(ele)
        self.count = self.count +1
    def stackpop(self):
        if not self.isStackEmpty():
            self.count -=1
            return self.data.pop()
        else:
            return None
    def StackPeek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return None
    def PrintElements(self):
        for i in range(-1,0):
            return self.data