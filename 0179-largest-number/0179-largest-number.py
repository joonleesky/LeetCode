class Solution(object):
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        
        merged = []
        i,j = 0,0
        while i <len(left) and j < len(right):
            left_val = left[i]
            right_val = right[j]
            
            left_num = int(left_val + right_val)
            right_num = int(right_val + left_val)
                    
            if left_num > right_num:
                merged.append(left_val)
                i += 1
            else:
                merged.append(right_val)
                j += 1
                
        merged += left[i:]
        merged += right[j:]
        
        return merged
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """        
        # exception
        is_zero = [num == 0 for num in nums]
        if sum(is_zero) == len(nums):
            return '0'
        
        nums = [str(num) for num in nums]        
        
        return ''.join(self.merge_sort(nums))