class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    if n == 0:
        return head 

    index = {}
    i = 0

    curr = head
    while curr:
        index[i] = curr
        curr = curr.next
        i += 1

    if i-n > 0 :
        index[i-n-1].next = index[i-n].next
    else:
        head = index[i-n].next

    return head
    # curr = head
    # while curr:
    #     print(curr.val)
    #     curr = curr.next


n=0
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(removeNthFromEnd(head, n))