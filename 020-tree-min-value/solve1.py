class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# depth first solution
def tree_min_value(root):
    if root is None:
        return float("inf")
    
    smallest_left_value = tree_min_value(root.left)
    smallest_right_value = tree_min_value(root.right)
    return min(root.val, smallest_left_value, smallest_right_value)


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