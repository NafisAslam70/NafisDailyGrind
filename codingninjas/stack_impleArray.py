class Stack:

    def __init__(self):
        self.__data=[]
        size=0

    def push(self, kyapush):
        self.__data.append(kyapush)

    def pop(self):
        if self.isEmpty():
            print("Stcak empty")
            return
        return self.__data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stcak empty")
            return
        ind=self.size()
        return self.data[ind-1]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size()==0
    
    
