class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def push(self, data):
        neww = Node(data)
        neww.next = self.__head
        self.__head = neww
        self.__count += 1

    def pop(self):
        # ? Bug: isEmpty is a method, so call it with ()
        if not self.isEmpty():
            d=self.__head.data
            self.__head = self.__head.next
            self.__count -= 1    # ? Don't forget to decrease count
            return d
        else:
            return -1          # ? Optional: indicate empty stack

    def top(self):
        if not self.isEmpty():   # ? fix: use ()
            return self.__head.data
        else:
            return -1          # ? Safe fallback