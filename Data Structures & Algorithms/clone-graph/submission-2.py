"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToCopy = {}

        def clone(node):

            if node in oldToCopy:
                return oldToCopy[node]

            copy = Node(node.val)
            oldToCopy[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node) if node else None