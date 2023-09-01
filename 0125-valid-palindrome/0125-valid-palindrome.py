class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # upper case to lower case
        s = s.lower()
        
        # remove non alpha-numeric
        s = list(s)
        _s = []
        for char in s:
            if char.isalnum():
                _s.append(char)
        
        s = ''.join(_s)
        rev_s = reversed(_s)        
        rev_s = ''.join(rev_s)
        
        if s == rev_s:
            return True
        else:
            return False
        