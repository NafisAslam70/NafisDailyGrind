# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def lengthLL(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def swapNodesByPos(self, head, i, j):
        if i == j:
            return head

        if i > j:
            i, j = j, i

        temp1 = head
        temp2 = head
        prev1 = None
        prev2 = None
        pos = 0

        while pos < i:
            prev1 = temp1
            temp1 = temp1.next
            pos += 1

        pos = 0
        while pos < j:
            prev2 = temp2
            temp2 = temp2.next
            pos += 1

        if prev1:
            prev1.next = temp2
        else:
            head = temp2

        if prev2:
            prev2.next = temp1

        # Swap next pointers
        temp = temp1.next
        temp1.next = temp2.next
        temp2.next = temp

        return head

    def swapNodes(self, head, k):
        length = self.lengthLL(head)
        i = k - 1
        j = length - k
        return self.swapNodesByPos(head, i, j)
