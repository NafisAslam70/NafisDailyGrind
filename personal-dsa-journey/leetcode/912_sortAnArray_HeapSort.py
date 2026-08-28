class Solution:

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def heapify(self, arr, n, pos):
        idx = pos

        while 2 * idx + 1 < n:

            g = idx
            left = 2 * idx + 1
            right = left + 1

            if arr[g] < arr[left]:
                g = left

            if right < n and arr[g] < arr[right]:
                g = right

            if g == idx:
                break

            self.swap(arr, g, idx)
            idx = g

    def sortArray(self, nums):

        n = len(nums)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # Heap sort
        for i in range(n - 1, 0, -1):
            self.swap(nums, 0, i)
            self.heapify(nums, i, 0)

        return nums