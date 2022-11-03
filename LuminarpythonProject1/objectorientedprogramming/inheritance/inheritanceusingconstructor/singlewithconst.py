class Person:       #parent class/super class/base class
    def __init__(self,name,age,place):
        self.n = name
        self.a =age
        self.p = place
class Student(Person):    #child class/subclass/derived clas
    dept = "cse"
    college = "ss college pothotta"
    def __init__(self,rollno,name,age,place):
        super().__init__(name,age,place)
        self.r=rollno
    def printdetails(self):
        print(self.n,self.a,self.p,"\nroll no =",self.r,"\ndepartment=",Student.dept,"\ncollege name=",Student.college)
s=Student(4,"adarsh",21,"kumbalam")
s.printdetails()