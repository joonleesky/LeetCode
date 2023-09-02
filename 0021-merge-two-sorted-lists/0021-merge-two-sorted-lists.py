# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    
        if (list1 is None) and (list2 is None):
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
    
        head, tail = None, None
        if list1.val < list2.val:
            head = tail = list1
            list1 = list1.next
        else:
            head = tail = list2
            list2 = list2.next
            
        while True:
            if list1 is None:
                tail.next = list2
                break
            
            elif list2 is None:
                tail.next = list1
                break
            
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next        
        
        return head
            