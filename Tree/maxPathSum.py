class Node:
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right= None

class BinaryTree:
  def __init__(self):
    self.root=None
    
  def insert(self,key):
    new_node=Node(key)
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
        
  def inOrder(self):
    res=[]
    stack=[]
    root=self.root
    while root or stack:
      while root:
        stack.append(root)
        root=root.left
      root=stack.pop()
      res.append(root.key)
      root=root.right
    return res
  
  def maxPathSum(self):
    maxi=[0]
    def traverse(node):
      if node is None:
        return 0
      l=max(0,traverse(node.left))
      r = max(0,traverse(node.right))
      maxi[0] = max(maxi[0],l+r+node.key)
      return node.key+max(l,r)
      
    
tree=BinaryTree()
for val in [-10,9,20,None,None,15,7]:
  tree.insert(val)
print(tree.inOrder())