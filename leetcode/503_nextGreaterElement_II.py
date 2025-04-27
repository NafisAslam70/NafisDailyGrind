class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        n=len(nums)
        ans=[-1]*n

        for i in range(0,n):
            curr=nums[i]
            while st and nums[st[-1]]<curr:
                ans[st[-1]]=curr
                st.pop()
            st.append(i)
        
        for i in range(0,n):
            curr=nums[i]

            while st and nums[st[-1]]<curr:
                ans[st[-1]]=curr
                st.pop()
        
        return ans


        