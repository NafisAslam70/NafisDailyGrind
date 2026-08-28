def findDuplicate(arr, n):
    seen = set()  # ? using set for fast lookup
    for i in arr:
        if i in seen:
            return i
        else:
            seen.add(i)

