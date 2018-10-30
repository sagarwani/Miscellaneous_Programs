#Implementation supports following operations:
#
#MyCircularQueue(k): Constructor, set the size of the queue to be k.
#Front: Get the front item from the queue. If the queue is empty, return -1.
#Rear: Get the last item from the queue. If the queue is empty, return -1.
#enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
#deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
#isEmpty(): Checks whether the circular queue is empty or not.
#isFull(): Checks whether the circular queue is full or not.

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.queue[0] = value
            self.head = 0
            self.tail = 0
            return True
        elif self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = value
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if (self.isEmpty()):
            return False
        elif (self.head == self.tail and self.head != -1):
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
            return True
        else:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if (self.head == -1 and self.tail == -1):
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (None not in self.queue):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
