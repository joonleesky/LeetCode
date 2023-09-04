# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        root = ListNode()
        root.next = head
        head = root
        
        cnt = 1        
        # traverse until left     
        while cnt < left:
            head = head.next
            cnt += 1
                    
        rev_root = head
        head = head.next
                
        # reverse until right
        while cnt < right:
            temp = head
            head = head.next
            temp.next = head.next
            head.next = rev_root.next
            rev_root.next = head
            head = temp
            cnt += 1
            
        return root.next