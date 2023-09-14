# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_diameter = 0
    
    def dfs(self, node):
        if node is None:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        diameter = left + right
        if diameter > self.max_diameter:
            self.max_diameter = diameter
            
        return max(left, right) + 1

    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.dfs(root)
        return self.max_diameter
