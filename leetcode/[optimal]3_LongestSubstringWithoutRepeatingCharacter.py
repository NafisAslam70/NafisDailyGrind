class Solution(object):

  def lengthOfLongestSubstring(self,s):
    char_index = {}
    max_len = 0
    start = 0

    for i, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= start:
            start = char_index[ch] + 1
        
        char_index[ch] = i
        max_len = max(max_len, i - start + 1)

    return max_len
