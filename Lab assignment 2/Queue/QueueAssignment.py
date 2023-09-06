from QueueAssigmentMethod import *

#Implement “Simple Queue” using list data structure.
def testEmptyStack():
    s1 = simpleQueue()
    print(s1.getCount())
    print(s1.isStackEmpty())

def testenQueue():
    s2 = simpleQueue()
    s2.enQueue(10)
    s2.enQueue(20)
    s2.enQueue(30) 
    print(s2.getCount())
    print(s2.QueuePeek())

def testdeQueue():
    s3 = simpleQueue()
    s3.enQueue(20)
    s3.enQueue(30)
    s3.enQueue(40)
    print(s3.deQueue())
    print(s3.getCount())

    

testEmptyStack()
testenQueue()
testdeQueue()