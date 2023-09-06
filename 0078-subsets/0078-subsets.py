class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # initialize
        subsets = [[]]
        queue = collections.deque([])
        for num in nums:
            queue.append([num])
        
        # traverse through bfs
        while len(queue) > 0:
            subset = queue.popleft()
            subsets.append(subset)
            
            for num in nums:
                if num > subset[-1]:
                    new_subset = list(subset) + [num]
                    queue.append(new_subset)
                    
        return subsets
            