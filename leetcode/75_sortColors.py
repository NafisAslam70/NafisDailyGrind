class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mid=0
        low=0
        high=len(nums)-1

        while mid<=high:
            n=nums[mid]

            if n==1:
                mid+=1
            elif n==0:
                nums[low], nums[mid]=nums[mid], nums[low]
                low+=1
                mid+=1
            else:
                nums[high], nums[mid]=nums[mid], nums[high]
                high-=1
            
        