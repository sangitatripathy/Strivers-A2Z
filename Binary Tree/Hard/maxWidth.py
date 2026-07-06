from collections import deque
def widthOfBinaryTree(self, root):
  queue = deque()
  maxWidth=0
  queue.append((root,0))

  while queue:
    size=len(queue)
    min_ind =queue[0][1]
    first=0
    last=0
    for i in range(size):
      node,idx = queue.popleft()
      curr_ind = idx-min_ind
      if i ==0:
        first=curr_ind
      if i==size-1:
        last = curr_ind
      if node.left:
        queue.append((node.left,(curr_ind*2)+1))
      if node.right:
        queue.append((node.right,(curr_ind*2)+2))
    maxWidth=max(maxWidth,last-first+1)
  return maxWidth
  