# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        pointer = root    
        
        # exception
        if head is None:
            return None
        elif head.next is None:
            return head
            
        while head:
            cur_node = head
            next_node = head.next
            if next_node is None:
                break
            next_next_node = head.next.next
            
            pointer.next = next_node
            pointer.next.next = cur_node
            pointer.next.next.next = next_next_node
            
            head = next_next_node
            pointer = pointer.next.next
    
        return root.next
        
        