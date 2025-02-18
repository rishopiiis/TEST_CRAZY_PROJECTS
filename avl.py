class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_tree(root, level=0, prefix="R----"):
    """Recursively prints the AVL tree in a structured format"""
    if root is not None:
        print(" " * (level * 4) + prefix + " " + str(root.key))
        if root.left or root.right:  # If there's at least one child, proceed
            print_tree(root.left, level + 1, "L----")
            print_tree(root.right, level + 1, "R----")

# Example Usage
root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(10)
root.left.right = Node(25)
root.right.right = Node(50)

print("Tree Structure of AVL Tree:")
print_tree(root)
