# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        fp = list1
        sp = list2
        newHead = None
        tail = None

        if list1 is None:
            return list2
        if list2 is None:
            return list1


        while fp is not None and sp is not None:
            if fp.val > sp.val:
                new_node = ListNode(sp.val)
                sp = sp.next
            else:
                new_node = ListNode(fp.val)
                fp = fp.next

            if newHead is None:
                newHead = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        while fp is not None:
            new_node = ListNode(fp.val)
            tail.next = new_node
            tail = new_node
            fp = fp.next

        while sp is not None:
            new_node = ListNode(sp.val)
            tail.next = new_node
            tail = new_node
            sp = sp.next

        return newHead
