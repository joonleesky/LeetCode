class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        permutations = []
        max_len = len(nums)
        
        # initialize queue
        queue = collections.deque([])
        for num in nums:
            queue.append([num])
        
        # traverse queue with bfs
        while len(queue) > 0:
            remain_nums = list(nums)
            permutation = queue.popleft()
            if len(permutation) == max_len:
                permutations.append(permutation)
                continue
            
            for num in permutation:
                remain_nums.remove(num)
                
            for num in remain_nums:
                cur_permutation = list(permutation)
                cur_permutation.append(num)
                queue.append(cur_permutation)
            
        return permutations
        