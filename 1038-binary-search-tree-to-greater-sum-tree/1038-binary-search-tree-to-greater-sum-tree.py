# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0
    
    def pre_order_traverse(self, node):
        if node:
            self.total += node.val
            
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)
            
    def in_order_traverse(self, node):
        if node.left:
            self.in_order_traverse(node.left)
        
        temp = node.val
        node.val = self.total
        self.total -= temp
        
        if node.right:
            self.in_order_traverse(node.right)
        
    
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.pre_order_traverse(root)
        self.in_order_traverse(root)
        
        return root
        