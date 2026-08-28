class MinStack(object):

    def __init__(self):
        self.a=[]
        self.b=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a.append(val)
        if not self.b or val <= self.b[-1]:   # ✅ notice <= not just <
            self.b.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        if self.a:
            if self.a[-1]==self.b[-1]:
                self.b.pop()
            self.a.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]
   


    def getMin(self):
        """
        :rtype: int
        """
        return self.b[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()