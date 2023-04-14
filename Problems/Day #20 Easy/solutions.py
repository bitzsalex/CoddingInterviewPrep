class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        

def find_intersection(head_a:Node, head_b:Node) -> Node:
    # check if both nodes are not empty
    if head_a == None or head_b == None: return None
    
    # initiate the pointer from each nodes
    a = head_a
    b = head_b
    
    # loop until a and b are equal
    while a != b:
        # when a reach to the end, reset it to point to head_b
        a = head_b if a == None else a.next
        # when b reach to the end, reset it to point to head_a
        b = head_a if b == None else b.next
        
    return a.data

# README: For more information on the solution, read: https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/49785/java-solution-without-knowing-the-difference-in-len/


# list 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)

#  list 2
head2 = Node(10)
head2.next = Node(9)
head2.next.next = Node(8)
head2.next.next.next = head1.next.next.next.next.next

find_intersection(head1, head2)