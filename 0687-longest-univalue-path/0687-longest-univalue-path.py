# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_length = 0
    
    def dfs(self, node, parent_val):
        if node is None:
            return 0            
        
        left = self.dfs(node.left, node.val)
        right = self.dfs(node.right, node.val)
        
        length = left + right
        if length > self.max_length:
            self.max_length = length
            
        if node.val == parent_val:
            return max(left, right) + 1
        else:
            return 0
        
    
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, -1)
        return self.max_length