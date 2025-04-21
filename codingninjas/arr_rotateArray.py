def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr, n, d):
    if n == 0 or d == 0:
        return

    d = d % n  # in case d > n
    reverse(arr, 0, d - 1)      # reverse first d
    reverse(arr, d, n - 1)      # reverse remaining
    reverse(arr, 0, n - 1)      # reverse whole

# ansarr=arr[d:0]+arr[:d]