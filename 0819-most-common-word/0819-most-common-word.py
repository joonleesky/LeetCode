class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        word_cnt = {}
        paragraph = re.sub(r'[^a-z^A-Z]', ' ',paragraph)
        
        for word in paragraph.split():
            low_word = word.lower()
           
            if low_word in banned:
                continue
            
            else:
                if low_word not in word_cnt:
                    word_cnt[low_word] = 1
                else:
                    word_cnt[low_word] += 1
                    
        max_cnt = 0
        common_word = ''
        for word, cnt in word_cnt.items():
            if cnt > max_cnt:
                common_word = word
                max_cnt = cnt
        
        return common_word