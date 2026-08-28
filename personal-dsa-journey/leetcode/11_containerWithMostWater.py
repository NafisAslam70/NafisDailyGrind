class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        
        ans=min(height[left], height[right])* (right-left)

        while left<=right:
            area= min(height[left], height[right])* (right-left)
            ans=max(ans,area)

            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        
        return ans

            