class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None] * k
        self.max_size = k
        self.num_in_buffer = 0
        self.root_idx = 0
        self.last_idx = -1
        
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.last_idx = (self.last_idx + 1)
            if self.last_idx >= self.max_size:
                self.last_idx = self.last_idx % self.max_size
            self.queue[self.last_idx] = value
            self.num_in_buffer = min(self.num_in_buffer+1, self.max_size)
            return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.root_idx] = None
            self.root_idx += 1
            if self.root_idx >= self.max_size:
                self.root_idx = self.root_idx % self.max_size
            self.num_in_buffer -= 1
            return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.root_idx]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.last_idx]        

        
    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.num_in_buffer == 0:
            return True
        else:
            return False
                

    def isFull(self):
        """
        :rtype: bool
        """
        if self.num_in_buffer == self.max_size:
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