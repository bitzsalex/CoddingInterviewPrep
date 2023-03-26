
# defining the node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
        
def preorder(node:Node):
    if node:
        print(node.val, end=", ")
        preorder(node.left)
        preorder(node.right)
        

def unival_counter(node:Node):
    if not node:
        return 0
    
    # check if it is a terminal node
    if node.left == node.right == None:
        return 1
    
    # if it is not binary balanced tree
    if not node.right and node.left.val == node.val:
        return 1 + unival_counter(node.left)
    elif not node.left and node.right.val == node.val:
        return 1 + unival_counter(node.right)
    elif node.val == node.left.val and node.val == node.right.val:
        return 1 + unival_counter(node.left) + unival_counter(node.right)
    
    return unival_counter(node.left) + unival_counter(node.right)


root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)


other = Node(9)
other.left = Node(8)
other.left.left = Node(8)
other.left.left.left = Node(8)
other.right = Node(9)
other.right.right = Node(9)
other.left.right = Node(7)
other.left.right.left = Node(7)
other.left.right.right = Node(7)

preorder(root)
unival_counter(root)

preorder(other)
unival_counter(other)