class Node():
    def __init__(self, value):
        self.value = value
        self.next = None           

def findLoop(head):
    if not head:
        return None
        
    slow = head.next
    fast = head.next.next
    prev = head
    
    counter = 1
    while slow != fast:
        slow = slow.next
        prev = fast
        fast = fast.next.next
        counter += 1

    if counter%2 != 0:
        return slow
    return prev



n0 = Node('n0')
n1 = Node('n1')
n2 = Node('n2')
n3 = Node('n3')
n4 = Node('n4')
n5 = Node('n5')
n6 = Node('n6')
n7 = Node('n7')
n8 = Node('n8')
n9 = Node('n9')

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n7

print(findLoop(n0).value)