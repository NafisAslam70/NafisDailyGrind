from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dd = deque()
        ans = []
        s = 0

        for i in range(len(nums)):

            # Remove all elements smaller than current
            while dd and nums[i] > dd[-1]:
                dd.pop()

            dd.append(nums[i])

            s += 1

            if s == k:
                ans.append(dd[0])

                # Now remove element if it is going out of the window
                if nums[i - s + 1] == dd[0]:
                    dd.popleft()

                s = s - 1  # manage window size correctly

        return ans
