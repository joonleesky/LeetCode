class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter_dict = {}
        for char in s:
            if char in counter_dict:
                counter_dict[char] += 1
            else:
                counter_dict[char] = 1
        
        stack = []
        for char in s:
            counter_dict[char] -= 1
            while True:
                if len(stack) == 0:
                    stack.append(char)
                    break
                else:
                    if char in stack:
                        break
                    else:
                        # remove the stack if there exists remaining
                        last_char = stack[-1]
                        if (char < last_char) and (counter_dict[last_char] > 0):
                            stack.pop()
                        else:
                            stack.append(char)
                            break                    
            
        s = ''.join(stack)       
        return s