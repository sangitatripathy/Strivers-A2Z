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

def balancedBinaryTree(root):
  if root is None:
    return False
  leftHeight= calcHeight(root.left)
  rightHeight=calcHeight(root.right)
  if abs(leftHeight-rightHeight) <=1 and balancedBinaryTree(root.left) and balancedBinaryTree(root.right):
    return True
  return False

def calcHeight(node):
  if node is None:
    return 0
  leftHeight=calcHeight(node.left)
  rightHeight=calcHeight(node.right)
  return max(leftHeight,rightHeight)+1
        