class Person:
    def __init__(self,name,age,place,phno):
        self.n=name
        self.a=age
        self.p=place
        self.ph=phno

class Parent(Person):
    def __init__(self,gender,address,name,age,place,phno):
        super().__init__(name,age,place,phno)
        self.g=gender
        self.ad=address

class Employee(Parent):
    company="luminar"
    def __init__(self,id,desig,salary,gender,address,name,age,place,phno):
        super().__init__(gender,address,name,age,place,phno)
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
        print("gender = ", self.g)
        print("address = ", self.ad)
        print("company name = ",Employee.company)

emp=Employee(4,"manager",23000,"male","blayithara","adarsh",21,"kakkanad",9087654367)
emp.printvalue()
