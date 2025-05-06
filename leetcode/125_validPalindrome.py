class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        n=len(s)
        r=n-1

        while l<=r:
            p=s[l].lower()
            q=s[r].lower()

            if not p.isalnum():
                l+=1
            elif not q.isalnum():
                r-=1
            elif p!=q:
                return False
            else:
                l+=1
                r-=1
        return True
