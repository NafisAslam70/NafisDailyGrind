def kReverse(head, k):
    if head is None or k == 1:
        return head

    # Step 1: Check if we have at least k nodes
    temp = head
    count = 0
    while temp and count < k:
        temp = temp.next
        count += 1

    # Step 2: Reverse k nodes
    currhead = head
    currtail = head
    t = k
    temp = head
    while t > 1:
        temp = temp.next
        t -= 1

    next_group_head = temp.next
    temp.next = None  # Break after k nodes

    revhead, revtail = reverseIterative(currhead)  # You already return both

    # Step 3: Recur for the rest of the list
    small = kReverse(next_group_head, k)
    revtail.next = small

    return revhead
def reverseIterative(head):
    prev=None
    curr=head

    while curr is not None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev,head