# single inheritance
class Person:       #parent class/super class/base class
    def setperson(self,name,age,place):
        self.n = name
        self.a =age
        self.p = place
class Student(Person):    #child class/subclass/derived clas
    dept = "cse"
    college = "ss college pothotta"
    def setstudent(self,rollno):
        self.r=rollno
    def printdetails(self):
        print(self.n,self.a,self.p,"\nroll no =",self.r,"\ndepartment=",Student.dept,"\ncollege name=",Student.college)
s=Student()
s.setperson("adarsh",21,"kumbalam")
s.setstudent(4)
s.printdetails()