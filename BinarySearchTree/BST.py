#Design data structure for Binary Search Tree. Write methods for adding node into B.
from SimpleQueue import *
class BST:
    class _node:
        def __init__(self,ele):
            self.data = ele
            self.left = None
            self.right = None
    def  __init__(self):
        self.root = None
        self.count = 0

    def isEmpty(self):
        return self.count ==0
    
    def getCount(self):
        return self.count
    
    def addNode(self,ele):
        cur = parent =self.root
        while cur != None and cur.data!= ele:
            parent = cur 
            if ele < cur.data:
                cur =  cur.left
            else:
                cur = cur.right

        if cur == None:
            new_node = self._node(ele)
            if parent == None:
                self.root = new_node
            elif ele < parent.data:
                parent.left = new_node
            elif ele > parent.data:
                parent.right = new_node
        self.count += 1

    def searchNode(self,ele):
        if not self.isEmpty():
            cur=self.root
            while(cur!=None):
                if(cur.data==ele):
                    break
                else:
                    if(cur.data>ele):
                        cur=cur.left
                    else:
                        cur=cur.right
            return cur!=None
        else:
            return False
#Inorder
    def Inorder(self):
        a = []
        if not self.isEmpty():
            self.inorder(self.root,a)
        return a

    def inorder(self,node,l):
        if node!= None:
            self.inorder(node.left,l)
            l.append(node.data)
            self.inorder(node.right,l)

#PreOrder 
    def PreOrder(self):
        a = []
        if not self.isEmpty():
            self.preorder(self.root,a)
        return a    

    def preorder(self,node,a):
        if node!= None:
            a.append(node.data)
            self.inorder(node.left,a)
            self.inorder(node.right,a)  
#PostOrder
    def PostOrder(self):
        a = []
        if not self.isEmpty():
            self.postorder(self.root,a)
        return a
    def postorder(self,node,a):
        if node!= None:
            self.postorder(node.left,a)
            self.postorder(node.right,a)
            a.append(node.data)

#Level Order

    def LevelOrder(self):
        if not self.isEmpty():
            l=[]
            q1=SimpleQueue()
            q1.enqueue(self.root)
            while not q1.isQueueEmpty():
                node=q1.dequeue()
                l.append(node.data)
                if node.left:
                    q1.enqueue(node.left)
                if node.right:
                    q1.enqueue(node.right)
            return l
        else:
            return None
        

#Write a method to count the nodes
    def getLeafNodeCount(self):
        if not self.isEmpty():
            return (self._LeafCount(self.root))
        else:
            return 0
        
    def _LeafCount(self,node):
        if node:
            if self.isLeafNode(node):
                return 1
            else:
                return(self._leafCount(node.left)+self._leafCount(node.right))
        else:
            return 0
        
    def isLeafNode(self, node):
        if node.left==None and node.right==None:
            return True
        else:
            return False

#Deleting a node 

    def deleteNode(self,key):
        if not self.isEmpty():
            self.root=self._nodeDelete(self.root,key)
            return self.count
        else:
            return None
    def _nodeDelete(self,node,key):
        if node==None:
            return None
        elif key<node.data:
            node.left=self._nodeDelete(node.left,key)
        elif key>node.data:
            node.right=self._nodeDelete(node.right,key)
        else:
            if node.left and node.right:
                temp=self._findMin(node.right)
                node.data=temp.data
                node.right=self._nodeDelete(node.right,temp.data)
            else:
                if node.right==None:
                    node=node.left
                    self.count-=1
                else:
                    node=node.right
                    self.count-=1
            
        return node
    def _findMin(self,node):
        if node.left==None:
            return node
        else:
            return self._findMin(node.left)



def test():
    B = BST()
    B.addNode(50)
    B.addNode(20)
    B.addNode(70)
    B.addNode(30)
    B.addNode(60)
    B.addNode(85)
    B.addNode(45)
    B.addNode(14)
    B.addNode(90)
    print(B.Inorder())
    print(B.PreOrder())
    print(B.PostOrder())
    print(B._LeafCount())
  #  assert(B.traverseDescendingOrder()==([60, 55, 50, 45, 40, 30, 25]))
   # assert(B.getHeight()==4)
    print(B.deleteNode(40))
    print(B.PreOrder())
    print(B.deleteNode(25))
   
   
    print(B.addNode(52))
    print(B.addNode(40))
    print(B.addNode(35))
    print(B.addNode(38))
    print(B._LeafCount())

test()
