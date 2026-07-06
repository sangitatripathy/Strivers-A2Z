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

def maxDepth(root):
  if root is None:
    return 0
  rootLeft=maxDepth(root.left)
  rootRight = maxDepth(root.right)
  return max(rootLeft,rootRight)+1

tree=BinaryTree()
for val in [10,20,30,40,50]:
  tree.insert(val)
print(maxDepth(tree.root))