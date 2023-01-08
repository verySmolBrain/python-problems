# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder, inorder):
            if len(preorder) == 0:
                return None

            node = TreeNode(preorder[0])
            node_idx = inorder.index(node.val)

            leftInorder, rightInorder = inorder[:node_idx], inorder[node_idx + 1:]
            leftPreorder, rightPreorder = [], []
            for n in preorder:
                if n in leftInorder: leftPreorder.append(n)
                if n in rightInorder: rightPreorder.append(n)

            node.left = construct(leftPreorder, leftInorder)
            node.right = construct(rightPreorder, rightInorder) 

            return node
        
        return construct(preorder, inorder)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            nodeVal = preorder.pop(0)
            ind = inorder.index(nodeVal)
            root = TreeNode(nodeVal)
            
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
        
        return None