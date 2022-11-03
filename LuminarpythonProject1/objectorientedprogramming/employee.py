# static variable related class   class name
# instance variable........related to methods ......instance keyword(self)
class Employee:
    company="luminar"
    def setvalue(self,id,name,desig,salary):
        self.i = id
        self.n = name
        self.d = desig
        self.s = salary
        # self.c = comp_name
    def printvalue(self):
        print("id = ",self.i)
        print("name = ",self.n)
        print("designation = ",self.d)
        print("salary = ",self.s)
        print("company name = ",Employee.company)
l=int(input("limit of instance created"))
for a in range(l):
    sa=Employee()
    i=int(input("enter your id"))
    n=input("enter your name")
    d=input("enter designation")
    s=input("enter your salary")
    # c=input("enter company name")
    sa.setvalue(i,n,d,s)
    sa.printvalue()