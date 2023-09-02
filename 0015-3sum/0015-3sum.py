class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return
        three_sum_list = []
        
        # sort based on ascending order
        nums = sorted(nums)

        # iterate
        for idx, val in enumerate(nums):
            left_idx = idx + 1
            right_idx = len(nums) - 1
            
            # two-pointer
            while left_idx < right_idx:
                left_val = nums[left_idx]
                right_val = nums[right_idx]
                
                three_sum_val = val + left_val + right_val
                if three_sum_val == 0:
                    three_sum = [val, left_val, right_val] 
                    if three_sum not in three_sum_list:
                        three_sum_list.append(three_sum)
                    left_idx += 1
                    right_idx -= 1
                    
                elif three_sum_val > 0:
                    right_idx -= 1
                    
                elif three_sum_val < 0:
                    left_idx += 1
    
        return three_sum_list