# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def split(self, node, arr):
        middle_idx = len(arr) // 2
        left = arr[:middle_idx]
        middle = arr[middle_idx]
        right = arr[middle_idx + 1:]
    
        node.val = middle
        if len(left) > 0:
            node.left = TreeNode()
            self.split(node.left, left)
        
        if len(right) > 0:
            node.right = TreeNode()
            self.split(node.right, right)        
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        root = TreeNode()
        self.split(root, nums)
        
        return root
        print(root.val)
        print(root.left.val)
        print(root.right.val)
        
        