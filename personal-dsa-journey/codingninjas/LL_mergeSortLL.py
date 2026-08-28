def mergeSort(head):
    if head is None or head.next is None:
        return head

    mid = midLL(head)
    second_half = mid.next
    mid.next = None  # ? This breaks the list properly

    left = mergeSort(head)
    right = mergeSort(second_half)

    return mergeTwoSortedLinkedLists(left, right)