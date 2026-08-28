def lengthRecursive(head):
    if head is None:
        return 0
    return 1+lengthRecursive(head.next)