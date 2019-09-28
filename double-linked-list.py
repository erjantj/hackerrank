class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not node:
            return
        if not self.head:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
            return 
        
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if not node:
            return 

        if not self.tail:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
            return 
        
        self.insertAfter(self.tail, node)
        
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
            
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert        

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return 

        node = self.head
        currPostition = 1
        while node and currPostition < position:
            node = node.next
            currPostition += 1

        if node == None:
            self.setTail(nodeToInsert)
            return

        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next

            if nodeToRemove.value == value:
                self.remove(node)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
            node.prev = None
        if node.next:
            node.next.prev = node.prev
            node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False


def printList(linked_list):
    node = linked_list.head
    while node:
        print(node.value, end=" ")
        node = node.next

    print()

    node = linked_list.tail
    while node:
        print(node.value, end=" ")
        node = node.prev

linked_list = DoublyLinkedList()

linked_list.setHead(Node(3))
linked_list.setHead(Node(2))
linked_list.setHead(Node(1))

linked_list.setTail(Node(4))
linked_list.setTail(Node(5))
linked_list.setTail(Node(6))

node = Node(11)
linked_list.insertAtPosition(10, node)
linked_list.insertBefore(node, Node(10))
linked_list.insertAfter(node, Node(12))

linked_list.remove(node)

print(linked_list.containsNodeWithValue(12))

printList(linked_list)