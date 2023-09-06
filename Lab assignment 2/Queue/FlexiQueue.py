from FlexiQueueMain import *

def testEmptyQueue():
    s1 = flexiQueue()
    print(s1.getFirst())
    print(s1.isEmpty())

def pushQueue():
    s2 = flexiQueue()
    s2.enQueue(10)
    s2.enQueue(20)
    s2.enQueue(30)
    s2.enQueue(40)
    s2.enQueue(50)
    print(s2.length())
    print(s2.getFirst())

def popQueue():
    s3 = flexiQueue()
    s3.enQueue(10)
    s3.enQueue(20)
    print(s3.getSize())
    s3.enQueue(30)
    print(s3.getSize())
    s3.deQueue()
    print(s3.getSize())
    s3.deQueue()
    print(s3.getSize())
    

testEmptyQueue()
pushQueue()
popQueue()