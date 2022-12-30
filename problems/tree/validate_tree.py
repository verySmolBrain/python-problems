# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, root)
    
    def validate(self, root, node):
        if node is None:
            return True
        
        if not self.search(root, node):
            return False
        
        return self.validate(root, node.left) and self.validate(root, node.right)
    
    def search(self, node, target):
        if node is None:
            return False
        
        if node == target:
            return True
        elif node.val > target.val:
            return self.search(node.left, target)
        elif node.val < target.val:
            return self.search(node.right, target)
        else:
            return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)
    
    def validate(self, node, floor, ceiling):
        if node is None:
            return True
        if node.val <= floor or node.val >= ceiling:
            return False
        
        return self.validate(node.left, floor, node.val) and self.validate(node.right, node.val, ceiling)