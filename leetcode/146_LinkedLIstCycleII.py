# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=head
        ins=None
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                ins=slow
                break
        if ins==None:
            return None
        else:
            while head!=ins:
                head=head.next
                ins=ins.next
            return head
        

        