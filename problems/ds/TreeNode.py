class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
    
    def bfs_create(nodes):
        nodes = iter(nodes)
        
        root = TreeNode(next(nodes, None))
        q = [root]
        
        while q:
            left, right = next(nodes, None), next(nodes, None)
            node = q.pop(0)
            
            if left != None:
                node.left = TreeNode(left)
                q.append(node.left)
            if right != None:
                node.right = TreeNode(right)
                q.append(node.right)

        return root

    
        