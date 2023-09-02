class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                # nothing to pop
                if len(stack) == 0:
                    return False
                
                # there exists parenthis to pop
                last = stack[-1]
                if last != match[char]:
                    return False
                stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False