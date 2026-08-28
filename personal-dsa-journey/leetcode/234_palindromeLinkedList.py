# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def lengthll(self,head):
        l=0
        while head is not None:
            l+=1
            head=head.next
        return l
    
    def reverseIterative(self,head):
        prev=None
        curr=head

        while curr is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l=self.lengthll(head)

        if l%2==0:
            mid=l//2
            p=mid
        else:
            mid=l//2+1
            p=mid-1
    
        temp=head
        k=0
        while k<mid and temp is not None:
            k+=1
            temp=temp.next
        revHead=self.reverseIterative(temp)
        
        fp=head
        sp=revHead


        while fp!=None and sp!=None and fp.val==sp.val and p>0:
            fp=fp.next
            sp=sp.next
            p-=1

        
        if p==0 or sp==None:
            return True
        else:
            return False




        