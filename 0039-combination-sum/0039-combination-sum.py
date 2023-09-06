class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # initialize
        combinations = []
        stack = []
        for num in candidates:
            if num == target:
                combinations.append([num])
            elif num > target:
                continue
            else:
                stack.append([num])    
        
        # search through dfs
        while len(stack) > 0:
            comb = stack.pop()
            sum_comb = sum(comb)
            
            for num in candidates:
                # return unique combinations
                # has to be incremental order
                if num < comb[-1]:
                    continue
                new_comb = list(comb) + [num]
                new_sum_comb = sum(new_comb)
                if new_sum_comb == target:
                    combinations.append(new_comb)
                elif new_sum_comb > target:
                    continue
                # new_sum_comb < target
                else:
                    stack.append(new_comb)
                    
        return combinations