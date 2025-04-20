def swapNodes(head, i, j):
    if i == j:
        return head

    if i > j:   # Swap to make sure i < j
        i, j = j, i

    temp1 = head
    temp2 = head
    prev1 = None
    prev2 = None
    pos = 0

    # Traverse to i-th node
    while pos < i:
        prev1 = temp1
        temp1 = temp1.next
        pos += 1

    pos = 0
    # Traverse to j-th node
    while pos < j:
        prev2 = temp2
        temp2 = temp2.next
        pos += 1

    # Edge Case: head change
    if prev1 is not None:
        prev1.next = temp2
    else:
        head = temp2  # swapping with head

    if prev2 is not None:
        prev2.next = temp1

    # Swap their nexts
    temp = temp1.next
    temp1.next = temp2.next
    temp2.next = temp

    return head


    