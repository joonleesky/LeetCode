class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # brute-force solution
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                
                if num1 + num2 == target:
                    return [i, j]
        """
        # hash-map solution
        hash_map = {}
        for idx, num in enumerate(nums):
            hash_map[num] = idx
            
        for idx, num in enumerate(nums):
            _target = target - num
            if _target in hash_map:
                trg_idx = hash_map[_target]
                if idx != trg_idx:
                    return [idx, hash_map[_target]]