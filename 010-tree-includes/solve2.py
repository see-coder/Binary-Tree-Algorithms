from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# breadth first solution
def tree_includes(root, target):
    if not root:
        return False
    
    queue = deque([ root ])
    
    while queue:
        node = queue.popleft()
        if node.val == target:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False


# Testing
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e")) # -> True

# n = number of nodes
# Time: O(n)
# Space: O(n)