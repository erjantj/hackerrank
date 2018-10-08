class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(node):
    if node.next:
        print(node.val, '->')
        printList(node.next)
    else:
        print(node.val)    

def addTwoNumbers(l1, l2, carry = 0):
    tmpSumm = l1.val+l2.val+carry
    nextNode = None

    summ = tmpSumm
    if summ > 9:
        summ = tmpSumm%10
        carry = tmpSumm//10
    else:
        carry = 0

    if l1.next and l2.next:
        nextNode = addTwoNumbers(l1.next, l2.next, carry)
    elif l1.next:
        nextNode = addTwoNumbers(l1.next, ListNode(0), carry)
    elif l2.next:
        nextNode = addTwoNumbers(ListNode(0), l2.next, carry)
    else:
        if carry:
            nextNode = ListNode(carry)

    node = ListNode(summ)  
    if nextNode:
        node.next = nextNode

    return node

# (5 -> 4 -> 3) + (5 -> 6 -> 4)
node1 = ListNode(8)
node2 = ListNode(1)

node3 = ListNode(0)

node2.next = node1

printList(addTwoNumbers(node2, node3))
