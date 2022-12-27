# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        traversal = []
        q.appendleft([root])

        while q:
            curLevel = q.pop()
            nextLevel = []
            levelValue = []

            for node in curLevel:
                if node is None:
                    continue
                nextLevel += [node.left, node.right]
                levelValue.append(node.val)
            
            if levelValue:
                traversal.append(levelValue)
            if nextLevel:
                q.appendleft(nextLevel)
    
        return traversal