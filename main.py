# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def compare(tree, search_value):
    current = tree

    while current.left is not None:
        current = current.left

    minimum = current.value

    current = tree

    while current.right is not None:
        current = current.right

    maximum = current.value

    if search_value < minimum:
        return "smaller"

    if search_value > maximum:
        return "bigger"

    return "spanned"


r"""
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9
"""
tree = Node(6, Node(3, Node(1), Node(5)), Node(8, None, Node(9)))
assert compare(tree, 10) == "bigger"
assert compare(tree, 0) == "smaller"
assert compare(tree, 4) == "spanned"
assert compare(tree, 1) == "spanned"
assert compare(tree, 5) == "spanned"
assert compare(tree, 9) == "spanned"


r"""
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             
   0               
"""
tree = Node(5, Node(3, Node(1, Node(0))), Node(7, None, Node(8)))
assert compare(tree, 9) == "bigger"
assert compare(tree, -1) == "smaller"
assert compare(tree, 0) == "spanned"
assert compare(tree, 8) == "spanned"

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
