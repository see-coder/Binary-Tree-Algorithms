from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# breadth first solution
def tree_sum(root):
    if not root:
        return 0
    
    queue = deque([ root ])
    total_sum = 0

    while queue:
        node = queue.popleft()
        total_sum += node.val
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return total_sum


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

print(tree_sum(a)) # -> 21

# n = number of nodes
# Time: O(n)
# Space: O(n)