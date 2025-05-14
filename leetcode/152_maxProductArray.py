class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxP=nums[0]
        minP=nums[0]

        result=nums[0]

        for j in range(1,len(nums)):

            if nums[j]>=0:
                maxP=max(nums[j],maxP*nums[j])
                minP=min(minP*nums[j], nums[j])
            else:
                temp=maxP
                maxP=max(nums[j],minP*nums[j])
                minP=min(nums[j],nums[j]*temp)

            result=max(result,maxP)
        
        return result


                                                                                                                                                                                  
