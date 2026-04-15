class Solution:
    def isSymmetric(self, root):    
        def isSymmetricHelp(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return (isSymmetricHelp(node1.left, node2.right) and
                    isSymmetricHelp(node1.right, node2.left))       
        return True if root is None else isSymmetricHelp(root.left, root.right)