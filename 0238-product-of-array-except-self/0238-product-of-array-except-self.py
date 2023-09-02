class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        left_prods = [prod]
        for num in nums[:-1]:
            prod *= num
            left_prods.append(prod)
            
        prod = 1
        right_prods = [prod]
        nums = list(reversed(nums))
        for num in nums[:-1]:
            prod *= num
            right_prods.append(prod)
        
        right_prods = list(reversed(right_prods))
        
        prods = []
        for i in range(len(nums)):
            left_prod = left_prods[i]
            right_prod = right_prods[i]
            
            prods.append(left_prod * right_prod)
        
        return prods
        