from typing import Optional
from ds.TreeNode import TreeNode

def isBalanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    
    if isBalanced(root.left) and isBalanced(root.right):
        return True
    else:
        return False
    
def depth(root: Optional[TreeNode]) -> int:
    if root:
        return 1 + max(depth(root.left), depth(root.right))
    else:
        return 0

def run():
    root = TreeNode.bfs_create([[3,9,20,None,None,15,7]])
    a = isBalanced(root)
    print(a)
    
    root = TreeNode.bfs_create([1,2,2,3,3,None,None,4,4])
    a = isBalanced(root)
    print(a)