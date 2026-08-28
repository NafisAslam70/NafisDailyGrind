def pairSum(arr, num):
    freq = {}
    count = 0

    for val in arr:
        complement = num - val
        if complement in freq:
            count += freq[complement]
        # Add val to freq after checking, to avoid self-pairing on same element
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    return count
