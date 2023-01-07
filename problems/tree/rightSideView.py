# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def getLeftNodeAtDepth(node, depth):
            if node is None:
                return None
            if depth <= 0:
                return node
            
            depth -= 1
            rightSide = getLeftNodeAtDepth(node.right, depth)
            leftSide = getLeftNodeAtDepth(node.left, depth)

            return rightSide if rightSide is not None else leftSide

        def traverseRight(root, node, path):
            if node is None:
                return
            path.append(node.val)
            
            if node.right is not None:
                traverseRight(root, node.right, path)
            elif node.left is not None:
                traverseRight(root, node.left, path)
            else:
                deeperNode = getLeftNodeAtDepth(root, len(path))
                traverseRight(root, deeperNode, path)
        
        p = []
        traverseRight(root, root, p)
        return p

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q, view = deque(), []
        if root:
            q.append(root)
        
        while q:
            size, val = len(q), 0

            for _ in range(size):
                node = q.popleft()
                val = node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            view.append(val)

        return view