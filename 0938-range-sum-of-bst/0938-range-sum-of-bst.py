# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0
    
    def collect(self, node, low, high):
        if node:
            val = node.val
            print(val, self.sum)
            if val < low:
                self.collect(node.right, low, high)
                
            elif (low <= val) and (val <= high):
                self.sum += val
                self.collect(node.left, low, high)
                self.collect(node.right, low, high)
            
            else:
                self.collect(node.left, low, high)
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.collect(root, low, high)
        return self.sum