# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(val=-float('inf'))
        root.next = head
        
        slow = root
        fast = root.next
        
        idx = 0
        while fast:
            val = fast.val
            temp_slow = root
            temp_fast = root.next
            
            replace = False
            temp_idx = 0
            while temp_idx < idx:
                temp_val = temp_fast.val
                
                if val < temp_val:
                    slow.next = fast.next
                    temp_slow.next = fast
                    fast.next = temp_fast
                    replace = True
                    break
                else:
                    temp_slow = temp_slow.next
                    temp_fast = temp_fast.next
                    temp_idx += 1
                    
            if replace:
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
            
            idx += 1
                
        return root.next
            
            