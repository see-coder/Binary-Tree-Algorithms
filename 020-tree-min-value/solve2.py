from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# breadth first solution
def tree_min_value(root):
    queue = deque([ root ])
    smallest = float("inf")
    
    while queue:
        current = queue.popleft()
        if current.val < smallest:
            smallest = current.val
        
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return smallest


# Testing
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_min_value(a)) # -> -2

# n = number of nodes
# Time: O(n)
# Space: O(n)