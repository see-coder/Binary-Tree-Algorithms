class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# depth first solution
def tree_includes(root, target):
    if not root:
        return False
    
    if root.val == target:
        return True
    
    return tree_includes(root.left, target) or tree_includes(root.right, target)


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