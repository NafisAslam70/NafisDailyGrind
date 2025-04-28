class Solution(object):

    def add2dc(self, e, dc):
        if e not in dc:
            dc[e] = 1
        else:
            dc[e] += 1
    
    def rem4dc(self, e, dc):
        dc[e] -= 1
        if dc[e] == 0:
            del dc[e]

    def strNotVal(self, dc):
        return any(val > 1 for val in dc.values())

    def lengthOfLongestSubstring(self, s):
        n = len(s)
        f = 0
        ans = 0
        dc = {}

        for c in range(n):
            self.add2dc(s[c], dc)

            while self.strNotVal(dc):  # Jab tak duplicate hai, window chhoti karo
                self.rem4dc(s[f], dc)
                f += 1

            ans = max(ans, c - f + 1)  # Update maximum length

        return ans
