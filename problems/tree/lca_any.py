# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCA(node, p, q):
            if node is None:
                return None
            if node == p or node == q:
                return node
            
            leftNode = findLCA(node.left, p, q)
            rightNode = findLCA(node.right, p, q)

            if leftNode and rightNode:
                return node
            elif leftNode and not rightNode:
                return leftNode
            elif rightNode and not leftNode:
                return rightNode
        
        return findLCA(root, p, q)