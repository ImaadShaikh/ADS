class maxHeap:
    def __init__(self,lst=[]):
        self.data = lst
        self._buildHeap() 

    def getCount(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) ==0
    
    def _parent_(self,i):
        return (i-1)//2
    
    def _lchild(self,i):
        return (2*i+1)
    
    def _rchild(self,i):
        return(2*i+2)
    
    def _swap_(self,i,j):
        self.data[i], self.data[j] =  self.data[j] , self.data[i]

    def _buildHeap(self):
        length = len(self.data)
        start = (length-2)//2
        for i in range(start,-1,-1):
            self._downHeap(i,length)

    def _downHeap(self,i,length):
        if self._lchild(i) < length:
            left = self._lchild(i)
            bigChild = left
            if self._rchild(i) < length:
                right = self._rchild(i)
                if self.data[bigChild] > self.data[i]:
                    self._swap_(bigChild,i)
                    self._downHeap(bigChild,length)

    def addElement(self,key):
        self.data.append(key)
        self._upHeap(len(self.data)-1)

    def _upHeap(self,j):
        parent= self._parent_(j)
        if j > 0 and self.data[j] > self.data[parent]:
         self._swap_(j,parent)
         self._upHeap(parent)

    def heapSort(self):
        if not self.isEmpty():
            for i in range(len(self.data)-1,0,-1):
                self._swap_(0,i)
                self._downHeap(0,i)
            return self.data


heap=maxHeap()
heap.addElement(50)
heap.addElement(10)
heap.addElement(15)
heap.addElement(60)
heap.addElement(90)
heap.addElement(5)
heap.addElement(75)

print(heap.getCount())
print(heap.heapSort())