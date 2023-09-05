# Implement with Separate Chaining

class KeyNode(object):
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap(object):

    def __init__(self):
        self.max_size = 10000 # at most call
        self.hash_map = []
        for _ in range(self.max_size):
            self.hash_map.append(KeyNode())
    
    def _hash_fn(self, key):
        return key % self.max_size
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_idx = self._hash_fn(key)
        head = self.hash_map[hash_idx]

        while head.key is not None:
            if head.key == key:
                head.value = value
                return None
            else:
                head = head.next
            
        head.key = key
        head.value = value
        head.next = KeyNode()

        return None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_idx = self._hash_fn(key)
        head = self.hash_map[hash_idx]
        while head.key is not None:
            if head.key == key:
                return head.value
            else:
                head = head.next

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_idx = self._hash_fn(key)
        head = self.hash_map[hash_idx]

        while head.key is not None:
            if head.key == key:
                head.key = head.next.key
                head.value = head.next.value
                head.next = head.next.next
                return -1
            else:
                head = head.next

        return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)