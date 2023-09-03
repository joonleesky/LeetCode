class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = [temperatures[0]]
        idx_list = [0]
        
        wait_list = [0] * len(temperatures)        
        for idx, temp in enumerate(temperatures[1:]):
            while True:
                if (len(stack) > 0) and (stack[-1] < temp):
                    stack.pop()
                    cur_idx = idx_list.pop()
                    wait_list[cur_idx] = (idx + 1 - cur_idx)
                else:
                    idx_list.append(idx+1)
                    stack.append(temp)
                    break
        
        return wait_list
                