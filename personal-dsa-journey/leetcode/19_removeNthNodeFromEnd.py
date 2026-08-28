# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        for i in range(n):
            fast=fast.next
        
        if fast is None:
            return head.next
        
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
   
        slow.next=slow.next.next
        
        return head

        