class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # initialize queue
        combinations = []
        queue = collections.deque([])
        total_nums = []
        for num in range(1, n+1):
            queue.append([num])
            total_nums.append(num)
            
        while len(queue) > 0:
            remain_nums = list(total_nums) # copy
            comb = queue.popleft()
            if len(comb) == k:
                combinations.append(comb)
                continue
                
            for num in comb:
                remain_nums.remove(num)
                
            for r_num in remain_nums:
                if r_num > comb[-1]:
                    new_comb = list(comb)
                    new_comb.append(r_num)
                    queue.append(new_comb)                
        
        return combinations
