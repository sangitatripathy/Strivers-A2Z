from collections import defaultdict
class Node:
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right= None

class BinaryTree:
  def __init__(self):
    self.root=None
    
  def insert(self,val):
    new_node=Node(val)
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

  def verticalTraversal(self):
    node=defaultdict(list)
    
    def dfs(root,row,col):
      if not root:
        return 
      node[col].append((row,root.val))
      dfs(root.left,row+1,col-1)
      dfs(root.right,row+1,col+1)
    dfs(self.root,0,0)
    res=[]
    for col in sorted(node.keys()):
      nodes=sorted(node[col])
      res.append([val for row,val in nodes])
    return res

tree=BinaryTree()
for val in [10,20,30,40,50]:
  tree.insert(val)
print(tree.verticalTraversal())