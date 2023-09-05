class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """            
        stones_dict = {}
        for stone in stones:
            if stone not in stones_dict:
                stones_dict[stone] = 1
            else:
                stones_dict[stone] += 1
        
        cnt = 0
        for jewel in jewels:
            if jewel in stones_dict:
                cnt += stones_dict[jewel]
        
        return cnt