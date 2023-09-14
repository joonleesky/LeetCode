# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.is_balanced = True
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
    
        if abs(left - right) > 1:
            self.is_balanced = False
                
        return max(left, right) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.dfs(root)
        return self.is_balanced
        