class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        word_cnt = {}
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-z]', ' ',paragraph)
        
        for word in paragraph.split():           
            if word in banned:
                continue
            
            else:
                if word not in word_cnt:
                    word_cnt[word] = 1
                else:
                    word_cnt[word] += 1
                    
        max_cnt = 0
        common_word = ''
        for word, cnt in word_cnt.items():
            if cnt > max_cnt:
                common_word = word
                max_cnt = cnt
        
        return common_word