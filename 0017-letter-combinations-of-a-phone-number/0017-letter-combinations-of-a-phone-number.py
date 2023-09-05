class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        digit2letters={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],            
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],            
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z']
        }
        
        _digits = []
        for digit in digits:
            _digits.append(digit)
        digits = _digits
        
        if len(digits) == 0:
            return []
        
        combinations = ['']
        while True:
            _combinations = []
            digit = digits.pop(0)
            letters = digit2letters[digit]
            for combination in combinations:
                for letter in letters:
                    _combinations.append(combination + letter)
            combinations = _combinations
            if len(digits) == 0:
                break
            
        return combinations