# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # exception
        if head is None:
            return head
        
        # init head
        odd_head = head
        even_head = head.next
        
        # init root
        odd_root = ListNode()
        odd_root.next = odd_head
        
        even_root = ListNode()
        even_root.next = even_head
        
        while True:
            if even_head is None:
                break
                                    
            elif even_head.next is None:
                break
            
            else:
                next_odd = odd_head.next.next
                next_even = even_head.next.next

                odd_head.next = next_odd
                even_head.next = next_even

                odd_head = next_odd
                even_head = next_even
        
        # connect
        odd_head.next = even_root.next
        return odd_root.next
            
        