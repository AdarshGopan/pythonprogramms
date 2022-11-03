class Person:
    def __init__(self,name,place,age):
        self.n=name
        self.p=place
        self.a=age
    def printvalue(self):
        print(self.n,self.p,self.a)
p=Person("adarsh","kumbalam",21)
p.printvalue()

p1=Person("amal","vellor",23)
p1.printvalue()
