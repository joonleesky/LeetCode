class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_str = ''
        str_dict = {}
        start_idx = 0
        for cur_idx, char in enumerate(s):
            if char not in str_dict:
                str_dict[char] = cur_idx
            else:
                cur_start_idx = str_dict[char] + 1
                if cur_start_idx > start_idx:
                    start_idx = cur_start_idx
                str_dict[char] = cur_idx
            
            cur_str = s[start_idx:cur_idx+1]
            if len(cur_str) > len(longest_str):
                longest_str = cur_str
        
        return len(longest_str)