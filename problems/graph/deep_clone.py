"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        originals, clones = deque([node]), {node.val: Node(node.val, [])}

        while originals:
            originalNode = originals.pop()
            clonedNode = clones[originalNode.val]

            for n in originalNode.neighbors:
                if n.val not in clones:
                    originals.appendleft(n)
                    clones[n.val] = Node(n.val, [])
                
                clonedNode.neighbors.append(clones[n.val])

        return clones[node.val]