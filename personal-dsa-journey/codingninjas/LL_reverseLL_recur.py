def reverseLinkedListRec(head) :
    if head is None:
        return None
    if head.next is None:
        return head
    
    small=reverseLinkedListRec(head.next)
    tail=small
    while tail.next is not None:
        tail=tail.next
    tail.next=head
    head.next=None
    return small