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
        
  def preOrder(self):
    res=[]
    stack=[self.root]
    while stack:
      node=stack.pop()
      res.append(node.key)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)
    return res

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

  def postOrder(self):
    res=[]
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        res.append(node.key)
    traverse(self.root)
    return res

tree=BinaryTree()
for val in [10,20,30,40,50]:
  tree.insert(val)
print(tree.preOrder())
print(tree.inOrder())
print(tree.postOrder())