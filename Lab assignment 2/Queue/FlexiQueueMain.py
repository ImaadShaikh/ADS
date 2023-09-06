class flexiQueue  :
    defaultSize = 2
    def __init__(self):
        self.data = [None]*flexiQueue.defaultSize
        self.count = 0
        self.front = 0
#checking the length and giving us the cout
    def length(self):
        return self.count
    
#checking if it is empty or not      
    def isEmpty(self):
        return self.count == 0

#giving us the first element 
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front] #L1[0]
        else:
            return None

#adding elements to the queue    
    def enQueue(self,ele):
        if self.count == len(self.data):
            self.resize(2*len(self.data))
        idx = (self.front + self.count)%len(self.data)
        self.data[idx] = ele
        self.count += 1
#deleting elements to the queue    
    def deQueue(self):
        if not self.isEmpty():
            ele = self.data[self.front]
            self.count -= 1
            self.data[self.front] = None
            # We are shrinking the value based on 
            self.front = (self.front +1)%len(self.data)
            if  0< (len(self.data) // 4):
                self.resize(len(self.data) // 2)
            return ele
        else:
            return None
# resizing the the element           
    def resize(self,cap):
        oldData = self.data
        walk = self.front
        self.data = [None]*cap
        for k in range(self.count):
            self.data[k] = oldData[walk]
            walk = (walk+1)%len(oldData) 
        self.front = 0
# checking the size of data
    def getSize(self):
        return len(self.data)


