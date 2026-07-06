class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    new_node = Node(key)
    if not self.root:
      self.root = new_node
      return
    queue = [self.root]
    while queue:
      temp = queue.pop(0)
      if not temp.left:
        temp.left = new_node
        return
      else:
        queue.append(temp.left)
      if not temp.right:
        temp.right = new_node
        return
      else:
        queue.append(temp.right)


class Solution:
  def isLeafNode(self, node):
    return node and not node.left and not node.right

  def leftBoundary(self, node, res):
    curr = node.left
    while curr:
        if not self.isLeafNode(curr):
            res.append(curr.key)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

  def rightBoundary(self, node, res):
    curr = node.right
    temp = []
    while curr:
        if not self.isLeafNode(curr):
            temp.append(curr.key)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    res.extend(temp[::-1])

  def addLeaf(self, node, res):
    if not node:
        return
    if self.isLeafNode(node):
        res.append(node.key)
        return
    self.addLeaf(node.left, res)
    self.addLeaf(node.right, res)

  def boundaryTraversal(self, root):
    if not root:
        return []

    res = []
    if not self.isLeafNode(root):
        res.append(root.key)

    self.leftBoundary(root, res)
    self.addLeaf(root, res)
    self.rightBoundary(root, res)

    return res


tree = BinaryTree()
for val in [10, 20, 30, 40, 50]:
    tree.insert(val)

sol = Solution()
print(sol.boundaryTraversal(tree.root))