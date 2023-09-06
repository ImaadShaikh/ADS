from LimitedQueue import *

def testEmptyStack():
    s1 = simplestack()
    print(s1.getCount())
    print(s1.isStackEmpty())

def testenQueue():
    s2 = simplestack()
    s2.enQueue(10)
    s2.enQueue(20)
    s2.enQueue(30) 
    s2.enQueue(40)
    s2.enQueue(50)
    s2.enQueue(60)
    print(s2.getCount())
    print(s2.StackPeek())

def testdeQueue():
    s3 = simplestack()
    s3.enQueue(20)
    s3.enQueue(30)
    s3.enQueue(40)
    s3.enQueue(71)
    s3.enQueue(90)
    s3.enQueue(100)
    print(s3.deQueue())
    print(s3.getCount())
    print(s3.PrintElements())

    

testEmptyStack()
testenQueue()
testdeQueue()

