class DoubleList:
    class _node_:
        def __init__(self,ele):
            self.data = ele 
            self.next = None
            self.prev = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def getCount(self):
        return self.count 
    
    def AddHeadElement(self, ele):
        new_node = self._node_(ele)
        if not self.isEmpty():
            new_node.next =  self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def AddTailElement(self,ele):
        new_node = self._node_(ele)
        if not self.isEmpty():
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
    
    def deleteHead(self):
        if not self.isEmpty():
            #print(self.head.data)
            data = self.head.data
            temp = self.head.next
            temp.prev = None
            self.head = temp
            if temp == None:
                self.tail = None
            self.count -=1 
        return data
    

        
    
    def deleteTail(self):
        if not self.isEmpty():
            data = self.tail.data
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
            if temp == None:
                self.head = None
            self.count -= 1
            return data
        else:
            return None
        
    def getElements(self):
        if not self.isEmpty():
            cur=self.head
            l=[]
            while(cur!=None):
                l.append(cur.data)
                cur=cur.next
            return l
        else:
            return None

list = DoubleList()
list.AddHeadElement(5)
list.AddHeadElement(10)
list.AddHeadElement(15)
list.AddTailElement(20)
list.AddTailElement(25)
print(list.getElements())
print(list.deleteHead())

#print(list.deleteHead()) #it is showing deleting 10
print(list.getElements())
#print(list.deleteTail())
#print(list.getElements())