class SimpleQueue:
    def __init__(self):
        self.data = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0
    
    def getCount(self):
        return self.count
    
    def enqueue(self,ele):
        self.data.append(ele)
        self.count+=1

    def dequeue(self):
        if not self.isEmpty():
            self.count -= 1
            return self.data.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            return None
        
    def print(self):
        return self.data