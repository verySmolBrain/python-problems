from ds.TreeNode import TreeNode

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

def run():
    root = TreeNode.bfs_create([6,2,8,0,4,7,9,None,None,3,5])
    a = lowestCommonAncestor(root, root.left, root.left.right)
    print(a.val)
    