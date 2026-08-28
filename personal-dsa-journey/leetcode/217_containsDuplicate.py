class Solution(object):
    def containsDuplicate(self, nums):
        return not (len(set(nums))==len(nums))