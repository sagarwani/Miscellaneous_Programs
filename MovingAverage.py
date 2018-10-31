#Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
#Example:
#
#MovingAverage m = new MovingAverage(3);
#m.next(1) = 1
#m.next(10) = (1 + 10) / 2
#m.next(3) = (1 + 10 + 3) / 3
#m.next(5) = (10 + 3 + 5) / 3

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = [None] * size
        self.tail = -1
        self.pos = 0
    
    def isEmpty(self):
        if self.tail == -1:
            return True

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        sumTotal1, sumTotal2 = 0,0
        self.flag = 0
        if self.isEmpty():
            self.queue[0] = val
            self.tail = 0
            self.pos += 1
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = val
            self.pos += 1
        #Calculate average
        if self.pos >= self.size:
            for i in range(self.size):
                sumTotal1 += self.queue[i]
            average = float(sumTotal1) / self.size
            return average
        else:
            for i in range(self.pos):
                sumTotal2 += self.queue[i]
            average = float(sumTotal2) / self.pos
            return average
        
            
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
