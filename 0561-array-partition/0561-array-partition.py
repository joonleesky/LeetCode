class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        
        sum_min_nums = 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                sum_min_nums += num
        
        return sum_min_nums
                
        