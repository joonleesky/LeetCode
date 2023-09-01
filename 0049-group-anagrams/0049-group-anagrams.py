from itertools import permutations

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word2idx = {}
        group_anagrams = None
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word2idx:
                anagram_idx = word2idx[sorted_word]
                group_anagrams[anagram_idx].append(word)
            
            if sorted_word not in word2idx:
                word2idx[sorted_word] = len(word2idx)
                
                if group_anagrams is None:
                    group_anagrams = [[word]]
                else:
                    group_anagrams.append([word])
                
        return group_anagrams