# to string
class Person:
    def __init__(self,name,place,age):
        self.age=age
        self.name=name
        self.place=place
    def printperson(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return str(self.age) + self.place     #self.name    returns name only
p=Person("anu","kumbalam",21)
print(p)
