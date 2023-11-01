class Node:
      def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None
class tree:

     def __init__(self):
           self.root=None

     def insert(self,data):
           if(self.root==None):
                  self.root=Node(data)
           else:
                  self._insert(data,self.root)


     def _insert(self, data, curNode):
           if(curNode.data>data):
                  if(curNode.left==None):
                         curNode.left=Node(data)

                  else:
                         self._insert(data,curNode.left)
           else:
                   if(curNode.right==None):
                         curNode.right=Node(data)
                   else:
                         self._insert(data,curNode.right)

f = Node(9)
print(f.__dict__)
x = tree()
print(x.__dict__)
x.insert(17)
print(x.__dict__)
