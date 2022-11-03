class Person:       #parent class/super class/base class
    def setperson(self,name,age,place):
        self.n = name
        self.a =age
        self.p = place
class Employee(Person):
    company="luminar"
    def setvalue(self,id,desig,salary):
        self.i = id
        self.d = desig
        self.s = salary
        # self.c = comp_name
    def details(self):
        print(self.n)
        print(self.a)
        print(self.p)
        print(self.i)
        print(self.d)
        print(self.s)
        print(Employee.company)
e1=Employee()
e1.setperson("adarsh",21,"kumbalam")
e1.setvalue(12,"manager",23000)
e1.details()