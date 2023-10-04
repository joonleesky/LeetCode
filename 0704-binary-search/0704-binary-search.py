class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary_search(left_idx, right_idx):
            if left_idx > right_idx:
                return -1
            
            mid_idx = (left_idx + right_idx) // 2            
            mid = nums[mid_idx]
            
            if target == mid:
                return mid_idx
            
            elif target < mid:
                return binary_search(left_idx, mid_idx-1)
                
            else:
                return binary_search(mid_idx+1, right_idx)
        
        idx = binary_search(0, len(nums)-1)
        
        return idx