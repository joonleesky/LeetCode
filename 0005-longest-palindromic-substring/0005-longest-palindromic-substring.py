class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        longest_pld = s[0]
        
        # when the length of palindrome is an odd number
        for middle_idx in range(len(s)):
            left_idx = middle_idx - 1
            right_idx = middle_idx + 1
            
            while True:
                if (left_idx < 0) or (right_idx >= len(s)):
                    break

                if s[left_idx] == s[right_idx]:
                    pld = s[left_idx: right_idx + 1]
                    if len(pld) > len(longest_pld):
                        longest_pld = pld
                    left_idx -= 1
                    right_idx += 1
                    
                else:
                    break
                
        # when the length of palindrome is an even number
        for middle_idx in range(len(s)):
            left_idx = middle_idx
            right_idx = middle_idx + 1
            
            while True:
                if (left_idx < 0) or (right_idx >= len(s)):
                    break

                if s[left_idx] == s[right_idx]:
                    pld = s[left_idx: right_idx + 1]
                    if len(pld) > len(longest_pld):
                        longest_pld = pld
                    left_idx -= 1
                    right_idx += 1
    
                else:
                    break
        
    
        
        return longest_pld
               
            
            
            
            
            
            