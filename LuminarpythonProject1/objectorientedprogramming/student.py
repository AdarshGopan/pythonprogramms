# static variable related class   class name
# instance variable........related to methods ......instance keyword(self)
class Student:
    dpt="computer science"    #static variable
    college_name="ss college"
    def setvalue(self,name,rollno):
        self.n=name
        self.r = rollno
        # self.d = dpt
        # self.c = college_name
    def printvalue(self):
        print(self.n)
        print(self.r)
        print(Student.dpt)
        print(Student.college_name)
for i in range(2):
    si=Student()
    n=input("enter your name")
    r=int(input("enter your roll no"))
    # d=input("enter department name")
    # c=input("enter college name")
    si.setvalue(n,r)
    si.printvalue()
