# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.arr = []
    
    def in_order_traverse(self, node):
        if node:
            if node.left:
                self.in_order_traverse(node.left)

            node_val = node.val
            self.arr.append(node.val)
            
            if node.right:
                right_val = self.in_order_traverse(node.right)
                    
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.in_order_traverse(root)
        
        min_diff = float('inf')
        for i in range(len(self.arr)-1):
            elem1, elem2 = self.arr[i], self.arr[i+1]
            diff = elem2 - elem1
            if diff < min_diff:
                min_diff = diff
    
        return min_diff