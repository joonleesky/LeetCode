# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        data = []
        queue = collections.deque([])
        queue.append((root))
        
        while len(queue) > 0:
            node = queue.popleft()
            if node:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append('#')
            data.append(',')
        
        """
        last_idx = float('inf')
        for idx, char in enumerate(data):
            if char != '#':
                last_idx = idx
                
        data = ''.join(data[:last_idx+1])
        """
        data = ''.join(data)
        
        return data 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split(',')
        
        root = TreeNode()
        
        depth_start, depth_end = 0, 1
        queue = collections.deque([root])
        
        idx = 0
        depth_idx = 0
        depth_start, depth_end= 0, 1
        depth_nodes = data[depth_start:depth_end]
        active_nodes = len(depth_nodes) - depth_nodes.count('#')
                
        while len(queue) > 0:
            node = queue.popleft()
            val = data[idx]
            
            if val != '#':
                node.val = int(val)
                left_idx = depth_end + depth_idx * 2
                right_idx = left_idx + 1
                
                if right_idx <= len(data):
                    if data[left_idx] == '#':
                        node.left = None
                    else:
                        node.left = TreeNode()
                    queue.append(node.left)
                        
                    if data[right_idx] == '#':
                        node.right = None
                    else:
                        node.right = TreeNode()
                    queue.append(node.right)
                depth_idx += 1
                
            idx += 1
            if idx >= depth_end:
                depth_start = depth_end
                depth_end = depth_end + active_nodes * 2
                depth_nodes = data[depth_start:depth_end]
                active_nodes = len(depth_nodes) - depth_nodes.count('#')
                depth_idx = 0
                
        return root
        
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))