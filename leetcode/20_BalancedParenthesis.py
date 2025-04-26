class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li=[]

        for char in s:
            if not li and char in ")}]":
                return False
            elif char in "[{(":
                li.append(char)
            
            elif char == ")" and li[-1] == "(":
                li.pop()
            elif char == "}" and li[-1] == "{":
                li.pop()
            elif char == "]" and li[-1] == "[":
                li.pop()
            else:
                return False  # ✅ mismatch case

        
        if not li:
            return True
        else:
            return False


        