# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head, node = None, None
        up = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            digit = val1 + val2 + up
            up = digit // 10
            remain = digit % 10
            
            temp = ListNode(val=remain, next=None)
            if node:
                node.next = temp
                node = node.next
            else:
                node = temp
                head = node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if up > 0:
            temp = ListNode(val=1, next=None)
            node.next = temp
            node = node.next
                
        return head