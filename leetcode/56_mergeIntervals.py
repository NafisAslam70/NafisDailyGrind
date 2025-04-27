class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()               # ✅ just sort
        self.intervals = intervals      # ✅ now assign
        ans = []
   
        ans.append(self.intervals[0])
    
        for t in self.intervals[1:]:
            if t[0] <= ans[-1][1]:                     # ✅ overlap
                ans[-1][1] = max(ans[-1][1], t[1])  # ✅ take max
            else:
                ans.append(t)
        return ans



