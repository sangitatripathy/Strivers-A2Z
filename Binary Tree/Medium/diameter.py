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

def diameter(node):
  if node is None:
    return 0
  lHeight=diameter(node.left)
  rHeight=diameter(node.right)
  return max(lHeight,rHeight)+1

tree=BinaryTree()
for val in [1,2,3,4,5]:
  tree.insert(val)

print(tree.inOrder())
diameter(tree.root)