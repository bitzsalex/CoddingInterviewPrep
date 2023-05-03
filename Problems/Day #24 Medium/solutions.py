class Node:
    def __init__(self) -> None:
        self.path = ""
        self.locked = False
        self.left = None
        self.right = None
        
        
def is_locked(node:Node) -> bool:
    return node.locked

def are_ancestors_unlocked(root:Node, node:Node) -> bool:
    head = root
    for direction in node.path:
        if is_locked(head): return False
        head = head.left if direction == "l" else head.right
    return True

def are_descendants_unlocked(node:Node) -> bool:
    if is_locked(node):
        return False
    
    if node.left and node.right:
        return are_descendants_unlocked(node.left) or are_descendants_unlocked(node.right)
    elif node.left:
        return are_descendants_unlocked(node.left)
    elif node.right:
        return are_descendants_unlocked(node.right)
    else:
        return True

def lock(root:Node, node:Node) -> bool:
    if are_ancestors_unlocked(root, node) and are_descendants_unlocked(node):
        node.locked = True
        return True
    
    return False


def unlock(root:Node, node:Node) -> bool:
    if are_ancestors_unlocked(root, node) and are_descendants_unlocked(node):
        node.locked = False
        return True
    
    return False
        
    
def add(parent:Node, direction:str="left") -> None:
    child = Node()
    if direction == "left":
        parent.left = child
        child.path = parent.path + "l"
    else:
        parent.right = child
        child.path = parent.path + "r"
        
        
head = Node()
add(head, "left")
add(head, "right")
add(head.left, "left")
add(head.left, "right")
add(head.right, "right")
add(head.left.left, "left")
add(head.left.left, "right")

lock(head, head.left)
lock(head, head.left.left.right)