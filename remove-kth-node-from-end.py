class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value
        
def printList(head):
    while head:
        print(head.value, end ='->')
        head = head.next
    print()

def getDepth(head):
    depth = 0
    while head:
        depth += 1
        head = head.next
    return depth

def removeKthNode(head, depth):
    if depth == 0:
        return head.next

    node = head
    parent = head
    while node and depth > 0:
        parent = node
        node = node.next
        depth -= 1
    
    parent.next = node.next
    return head
    
def removeKthNodeFromEnd(head, k):
    if not head or k == 0:
        return head
    
    depth = getDepth(head)
    remove_depth = depth - max(0,k)
    
    return removeKthNode(head, remove_depth)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

printList(head)
printList(removeKthNodeFromEnd(head, 10))