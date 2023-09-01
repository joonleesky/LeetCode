class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1
        
        while True:
            if left >= right:
                break
            else:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                
                left = left + 1
                right = right - 1