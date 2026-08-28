def tripletSum(arr, n, num):
    count = 0
    for i in range(n):
        target = num - arr[i]
        count += pairSum(arr[i+1:], target)
    return count

def pairSum(arr, num):
    freq = {}
    count = 0

    for val in arr:
        complement = num - val
        if complement in freq:
            count += freq[complement]
        # Add val to freq after checking
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    return count
