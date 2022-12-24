# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_diameter = self.maxDepth(root.right) + self.maxDepth(root.left)

        return max(max_diameter, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
    
    def maxDepth(self, node: TreeNode) -> int:
        if node == None:
            return 0
        else:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))