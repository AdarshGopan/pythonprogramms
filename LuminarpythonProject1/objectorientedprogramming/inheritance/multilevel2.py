class Person:
    def setperson(self,name,age,place,phno):
        self.n=name
        self.a=age
        self.p=place
        self.ph=phno

class Parent(Person):
    def setparent(self,gender,address):
        self.g=gender
        self.ad=address
    def printparent(self):
        print("gender = ",self.g)
        print("address = ",self.ad)

class Employee(Parent):
    company="luminar"
    def setemp(self,id,desig,salary):
        self.i = id
        self.d = desig
        self.s = salary
    def printvalue(self):
        print("id = ", self.i)
        print("name = ",self.n)
        print("age = ",self.a)
        print("place = ",self.p)
        print("phno = ",self.ph)
        print("designation = ",self.d)
        print("salary = ",self.s)
        print("company name = ",Employee.company)

emp=Employee()
emp.setperson("adarsh",21,"kakkanad",9087654367)
emp.setparent("male","blayithara")
emp.setemp(4,"manager",23000)
emp.printvalue()
emp.printparent()