# given class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# MY SOLUTION BELOW
# ===========================
def serialize(node: Node):
    # pre-order serialization
    if node == None:
        # place '#' symbol in place of None Values
        return "#"
    
    # concatenate all the values together to form single string
    return node.val + "," + serialize(node.left) + "," + serialize(node.right)


def _deserialize(node_list:list):
    # check if the node list isn't empty
    if not node_list:
        return None
    
    # pop the first node value (element from the list)
    value = node_list.pop(0)
    root = None
    
    # if the value is not empty, create a note and call the
    # _deserialize function for it's left and right children
    if value != "#":
        root = Node(value)
        root.left = _deserialize(node_list)
        root.right = _deserialize(node_list)
    
    # return the node
    return root


def deserialize(serialized: str):
    # split the serialized string and call `_deserialization` function
    return _deserialize(serialized.split(",")) if serialized else None


def preorder_traversal(root):
    if root:
        print(root.val, end=', ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)


node = Node('root', Node('left', Node('left.left')), Node('right'))
preorder_traversal(node)


serialized = serialize(node)
print(serialized)

reverted = deserialize(serialized)
preorder_traversal(reverted)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
