# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # exception
        if root is None:
            return 0
        
        # traverse through bfs
        max_depth, depth = 1, 1
        queue = collections.deque([])
        queue.append((root, depth))
        
        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
                
        return max_depth