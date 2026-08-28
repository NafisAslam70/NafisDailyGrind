class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ms = set(nums)
        ans = 0

        for e in ms:
            if e - 1 not in ms:  # only start new sequence
                c = 1
                while e + 1 in ms:
                    c += 1
                    e += 1
                ans = max(ans, c)

        return ans
