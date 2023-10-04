class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # two-pointer: O(n)
        i, j = 0, len(numbers)-1
        
        while True:
            left = numbers[i]
            right = numbers[j]
            
            two_sum = left + right
            if two_sum == target:
                return [i+1,j+1]
            elif two_sum > target:
                j -= 1
            else:
                i += 1