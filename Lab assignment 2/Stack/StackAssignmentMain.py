#from LimitedMemoryAssignment import *
from stackassignment import *

#QUESTION 1
def testEmptyStack():
    s1= simplestack()
    print(s1.getCount())
    print(s1.isStackEmpty())

def testpush():
    s2 = simplestack()
    s2.StackPush(10)
    print(s2.getCount())
    print(s2.StackPeek())

def testpop():
    s3 = simplestack()
    s3.StackPush(20)
    s3.StackPush(30)
    s3.StackPush(40)
    assert(s3.getCount()==3)
    assert(s3.stackpop()==40)

#question 2
#stack = simplestack()

#def testEmptyStack():
 #   s1 = simplestack()
  #  print(s1.getCount())
   # print(s1.isStackEmpty())

#def testpush():
 #   s2 = simplestack()
  #  s2.StackPush(10)
   # s2.StackPush(20)
    #s2.StackPush(30)
    #s2.StackPush(40)
    #s2.StackPush(50)
    #print(s2.isStackFull())
    #s2.StackPush(60)
    #print(s2.count)
    #print(s2.StackPeek()) 

testEmptyStack()
testpush()
testpop()
