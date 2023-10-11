class LinkedList:
    class _node_:
        def __init__(self,ele):
            self.data = ele
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0
    
    def getCount(self):
        return self.count
    
    def addAtHead(self,ele):
        new_node = self._node_(ele)
        if not self.isEmpty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count+= 1

    def addAtTail(self,ele):
        new_node = self._node_(ele)
        if not self.isEmpty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def DeleteHead(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            if self.head is None :
                self.tail = None
            self.count -=1
            return data
        else:
            return None

    def DeleteTail(self):
        if not self.isEmpty():
            if self.count >= 1 :
                cur = self.head
                last = self.tail
                while cur.next != last :
                    cur = cur.next
                self.tail = cur
                cur.next = None
            else:
                self.head = self.tail = None
            self.count -= 1
            return cur.data
        else:
            return None
        
    def getElements(self):
        list=[]
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                list.append(cur.data)
                cur=cur.next
            return list


list= LinkedList()
list.addAtHead(10)
list.addAtTail(20)
list.addAtHead(5)
list.addAtHead(30)
list.addAtTail(65)
print(list.getCount())
print(list.getElements())
list.DeleteHead()
print(list.getElements())
list.DeleteTail()
print(list.getElements())
