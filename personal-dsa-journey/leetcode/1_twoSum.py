class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i,e in enumerate(nums) :
            n= (target-e)
            if n in seen:
                return [i,seen[n]]
            else:
                seen[e]=i


