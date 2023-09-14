# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:
            root1.val = root1.val + root2.val
        
        elif root1:
            return root1
        
        elif root2:
            return root2
        
        else:
            return None
        
        queue = collections.deque([(root1, root2)])
        while len(queue) > 0:
            node1, node2 = queue.pop()
            
            if node1.left and node2.left:
                node1.left.val = node1.left.val + node2.left.val
                queue.append((node1.left, node2.left))
            
            elif node1.left:
                pass
            
            elif node2.left:
                node1.left = node2.left
                
            else:
                pass
            
            if node1.right and node2.right:
                node1.right.val = node1.right.val + node2.right.val
                queue.append((node1.right, node2.right))
            
            elif node1.right:
                pass
            
            elif node2.right:
                node1.right = node2.right
                
            else:
                pass
            
                
        return root1