#Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#
#Implement these functions in your linked list class:
#
#get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#addAtTail(val) : Append a node of value val to the last element of the linked list.
#addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size or self.head == None:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node1 = Node(val)
            node1.next = self.head
            self.head = node1
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            cur = Node(val)
            self.tail = cur
            self.head = self.tail
        else:
            cur = Node(val)
            self.tail.next = cur
            self.tail = cur
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size or index < 0:
            return -1
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node1 = Node(val)
            node1.next = cur.next
            cur.next = node1
            if node1.next == None:
                self.tail = node1
        
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.size or index < 0 or self.head == None:
            return -1
        elif index == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            tmp = cur.next
            cur.next = tmp.next
            if cur.next == None:
                self.tail = cur
        self.size -= 1
            
  


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
