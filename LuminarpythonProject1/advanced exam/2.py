class Person:
    def setperson(self,name,age):
        self.n=name
        self.a=age
    def getperson(self):
        print(self.n)
        print(self.a)
class Student(Person):  #single inheritance
    dept = "computer science"
    def setstudent(self,id):
        self.i=id
    def getstudent(self):
        print(Student.dept)
        print(self.i)
class Teenager(Student):      #multi level inheritance
    def setteenager(self):
        print('teenager class')
class Adult:
    def setadult(self):
        print('adult class')
class Employee(Person,Adult):    #multiple inheritance
    def setemployee(self,eid):
        self.eid=eid
    def getemployee(self):
        print(self.eid)
s=Student()
s.setstudent(1)
s.getstudent()
s.setperson("adarsh",21)
s.getperson()

t=Teenager()
t.setstudent(34)
t.getstudent()
t.setteenager()

e=Employee()
e.setemployee(12)
e.getemployee()
e.setadult()
e.setperson("ambu",23)
e.getperson()



