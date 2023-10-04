class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # exception
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
    
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        
        # search pivot
        # pivot can be found based on the reverse of order
        def search_pivot(left_idx, right_idx):
            if left_idx > right_idx:
                return -1
            
            mid_idx = (left_idx + right_idx) // 2
            
            # pivot is here
            if (nums[mid_idx-1] < nums[mid_idx]) and (nums[(mid_idx+1)%len(nums)] < nums[mid_idx]):
                return mid_idx
            
            else:
                if nums[left_idx] > nums[mid_idx]:
                    return search_pivot(left_idx, mid_idx-1)
                else:
                    return search_pivot(mid_idx+1, right_idx)          
                    
        pivot_idx = search_pivot(0, len(nums)-1)
        
        # search target based on pivot
        def search_target(left_idx, right_idx):
            if left_idx > right_idx:
                return -1
            
            mid_idx = (left_idx + right_idx) // 2
            p_mid_idx = (mid_idx + pivot_idx + 1) % len(nums)
                      
            mid = nums[p_mid_idx]
                
            if mid == target:
                return p_mid_idx
            elif mid > target:
                return search_target(left_idx, mid_idx-1)
            else:
                return search_target(mid_idx+1, right_idx)
        
        target_idx = search_target(0, len(nums)-1)
        
        return target_idx
        
        
        
        
        