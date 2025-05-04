# parent class
class Person():
    # write your code logic !!
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
       print("{} {}".format(self.name, self.age))





# child class
class Student(Person):
    # write your code logic !!'
    def __init__(self, name, age, dob):
        super().__init__(name,age)
        self.dob=dob
    
    def displayInfo(self):
        print("{} {} {}".format(self.name, self.age, self.dob))


    

obj = Student("Rahul", 23, "16-03-2000")
obj.display()
obj.displayInfo()
