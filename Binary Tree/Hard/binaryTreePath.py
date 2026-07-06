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

def binaryTreePaths(root):
  def isLeafNode(node):
    return not node.left and not node.right
  res=[]
  def traverse(node,temp):
    temp.append(node.key)
    if isLeafNode(node):
      res.append("->".join(map(str,temp)))
    else:
      if node.left:
          traverse(node.left,temp)
      if node.right:
          traverse(node.right,temp)
    temp.pop()
  traverse(root,[])
  return res

tree=BinaryTree()
for val in [10,20,30,40,50]:
  tree.insert(val)
print(binaryTreePaths(tree.root))