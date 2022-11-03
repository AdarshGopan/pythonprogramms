class Person:
    def __init__(self,name,age,place,phno):
        self.n=name
        self.a=age
        self.p=place
        self.ph=phno
class Child:
    std="+2"
    def __init__(self,school_name):
        self.sch=school_name
        # self.std=std
    def printChild(self):
        print(self.sch)
        print(Child.std)
class Student(Person,Child):
    dpt="cse"
    col_name="ss college poothotta"
    def __init__(self,name,age,place,phno,roll,mark,school_name):
        Person.__init__(self,name,age,place,phno)
        Child.__init__(self,school_name)
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

s1=Student("adarsh",21,"kumbalam",90876543210,4,50,"srv higher secondary school")
s1.printChild()
s1.details()