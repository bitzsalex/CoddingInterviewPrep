
class Node:
    """A Node object"""
    def __init__(self, value:str) -> None:
        self.locked = False
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
        self.is_any_children_locked = False
        
    def is_locked(self) -> bool:
        return self.locked
    
    def lock(self) -> None:
        if self.is_locked() or self.is_any_children_locked \
            or self.is_there_any_locked_ancestor():
            return False
        
        self.locked = True
        self.update_ancestors("locked")
        return True
    
    def unlock(self) -> bool:
        if not self.is_locked() or self.is_any_children_locked \
            or self.is_there_any_locked_ancestor():
            return False
        
        self.locked = False
        self.update_ancestors("unlocked")
        return True
    
    def update_ancestors(self, operation:str) -> None:
        current_node = self.parent
        while current_node:
            current_node.is_any_children_locked = True if operation == "locked" else False
            current_node = current_node.parent
    
    def is_there_any_locked_ancestor(self) -> bool:
        current_node = self.parent
        while current_node:
            if current_node.is_locked(): return True
            current_node = current_node.parent
            
        return False
    
    def add(self, value:str, direction:str="left") -> None:
        child = Node(value)
        if direction == "left":
            self.left = child
        else:
            self.right = child
        
        child.parent = self    
        return child
        
        
head = Node("root")
l1 = head.add("l1", "left")
r1 = head.add("l2", "right")

l1l1 = l1.add("l1l1", "left")
l1r1 = l1.add("l1r1", "right")

r1r1 = r1.add("r1r1", "right")
l1l2 = l1l1.add("l1l2", "left")


l1l1.lock()  # True
l1l2.lock()  # False
head.lock()  # False
head.is_any_children_locked  # True

l1l1.unlock()  # True
l1l2.lock()  # True