class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList( head):
    if not head:
        return head

    if not head.next:
        return head

    last_odd = None
    last_even = None
    first_odd = None
    first_even = None
    
    counter = 1
    while head:
        if counter%2 != 0:
            if not first_odd:
                first_odd = head
            if not last_odd:
                last_odd = head
            else:
                last_odd.next = head
                last_odd = head
        else:
            if not first_even:
                first_even = head
            if not last_even:
                last_even = head
            else:
                last_even.next = head
                last_even = head
        counter += 1
        head = head.next
    last_even.next = None
    last_odd.next = first_even
    
    return first_odd

# [1,2,3,4,5]
a1 = ListNode(1)
a2 = ListNode(2)
# a3 = ListNode(3)
# a4 = ListNode(4)
# a5 = ListNode(5)

a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5

head = oddEvenList(a1)

while head:
    print(head.val)
    head = head.next