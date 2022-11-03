#person  name,age,place,phno
#child   school_name,std
#student roll_no,dept,mark
class Person:
    def setperson(self,name,age,place,phno):
        self.n=name
        self.a=age
        self.p=place
        self.ph=phno
class Child:
    std="+2"
    def setchild(self,school_name):
        self.sch=school_name
        # self.std=std
    def printChild(self):
        print(self.sch)
        print(Child.std)
class Student(Person,Child):
    dpt="cse"
    col_name="ss college poothotta"
    def setstudent(self,roll,mark):
        self.r=roll
        self.m=mark
    def details(self):
        print(self.n)
        print(self.a)
        print(self.p)
        print(self.ph)
        print(self.r)
        print(self.m)
        print(Student.dpt)
        print(Student.col_name)

s1=Student()
s1.setperson("adarsh",21,"kumbalam",90876543210)
s1.setchild("srv higher secondary school")
s1.setstudent(4,50)
s1.printChild()
s1.details()