class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # i: row
        # j: col
        num_row = len(matrix)
        num_col = len(matrix[0])
        
        i, j = 0, 0
        
        while (-1 < i < num_row) and (-1 < j < num_col):
            val = matrix[i][j]
            
            if val == target:
                return True
            
            elif val < target:
                if (j+1) < num_col:
                    if matrix[i][j+1] <= target:
                        j += 1
                    else:
                        i += 1
                else:
                    i += 1
            else:
                j -=1
        
        return False