class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # Skip duplicate starting points
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res
