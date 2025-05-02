class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        else:
            s1={}

            for e in s:
                if e not in s1:
                    s1[e]=1
                else:
                    s1[e]+=1
            
            for e in t:
                if e not in s1:
                    return False
                else:
                    s1[e]-=1
            
            return all(v == 0 for v in s1.values())


            a