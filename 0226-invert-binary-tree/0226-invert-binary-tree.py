# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        queue = collections.deque([])
        queue.append(root)
        
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                continue
                
            temp = node.left
            node.left = node.right
            node.right = temp
            queue.append(node.left)
            queue.append(node.right)
                    
        return root