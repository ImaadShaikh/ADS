from stackassignment import *

def testSymbols(value):
    lefty = '{[('
    righty = '}])'
    s1 = simplestack()
    
    for i in value:
        f=0
        if i in lefty:
            s1.StackPush(i)
        else:
            if not s1.isStackEmpty():
                ele = s1.stackpop()
                if not (righty.index(i) == lefty.index(ele)):
                    f=1
                    break
            
            else:
                f = 1
                break

                
    if(f==1):
        return False
    else:
        return True
    
print(testSymbols("({[})") )          