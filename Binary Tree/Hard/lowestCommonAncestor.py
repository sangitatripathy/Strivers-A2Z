def lca(root,p,q):
  if root is None:
    return None
  if root == p or root == q:
    return root
  left = lca(root.left,p,q)
  right = lca(root.right,p,q)
  if left and right:
    return root
  return left if left else right