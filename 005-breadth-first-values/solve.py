from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    if not root:
        return []
    
    queue = deque([ root ])
    values = []
    
    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return values


# Testing
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

print(breadth_first_values(a)) # -> ['a', 'b', 'c', 'd', 'e', 'f']

# n = number of nodes
# Time: O(n)
# Space: O(n)