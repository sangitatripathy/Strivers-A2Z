class Node:
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None

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

  def preOrder(self,node):
    if node == None:
      return
    print(node.key,end=" ")
    self.preOrder(node.left)
    self.preOrder(node.right)

  def inOrder(self,node):
    if node == None:
      return
    self.inOrder(node.left)
    print(node.key,end=" ")
    self.inOrder(node.right)

  def postOrder(self,node):
    if node == None:
      return
    self.postOrder(node.left)
    self.postOrder(node.right)
    print(node.key,end=" ")
    
    

tree=BinaryTree()
for val in [10,20,30,40,50,60]:
  tree.insert(val)

print("inorder traversal")
tree.inOrder(tree.root)

print("\nPreorder traversal")
tree.preOrder(tree.root)

print("\nPostorder Traversal")
tree.postOrder(tree.root)