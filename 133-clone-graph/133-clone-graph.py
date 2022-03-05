"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node == None : return None
        cloneMap = {}

        def cloneHelp(node) :
            
            clone = Node(node.val)
            cloneMap[node] = clone
            
            neighbors = node.neighbors
            for neighbor in neighbors :
                    if neighbor in cloneMap.keys() :
                        clone.neighbors.append(cloneMap[neighbor])
                    else:
                        clone.neighbors.append(cloneHelp(neighbor))
                        
            return clone
        return cloneHelp(node)