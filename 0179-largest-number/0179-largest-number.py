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
            left_num = int(left[i] + right[j])
            right_num = int(right[j] + left[i])
                    
            if left_num > right_num:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
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