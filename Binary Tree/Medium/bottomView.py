from collections import defaultdict
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right= None

class BinaryTree:
  def __init__(self):
    self.root=None
    
  def insert(self,data):
    new_node=Node(data)
    if not self.root:
      self.root=new_node
      return
    queue=[self.root]
    while(queue):
      temp=queue.pop(0)
      if not temp.left:
        temp.left=new_node
        return
      else:
        queue.append(temp.left)
      if not temp.right:
        temp.right=new_node
        return
      else:
        queue.append(temp.right)
        
class Solution:
    def bottomView(self, root):
      res=[]
      dict=defaultdict(list)
      def traversal(root,row,col):
        if not root:
          return
        if col not in dict or row >= dict[col][0]:
          dict[col] = (row,root.data)
        traversal(root.left,row+1,col-1)
        traversal(root.right,row+1,col+1)
      traversal(root,0,0)
      for col in sorted(dict):
        res.append(dict[col][1])
      return res
tree=BinaryTree()
for val in [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]:
  tree.insert(val)
sol=Solution()
sol.bottomView(tree.root)