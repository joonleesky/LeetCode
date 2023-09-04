class MyStack(object):

    def __init__(self):
        self.queue = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        _queue = [0] * len(self.queue)
        for idx, item in enumerate(self.queue):
            _idx = (idx + 1) % len(self.queue)
            _queue[_idx] = item
        self.queue = _queue
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.queue) == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()