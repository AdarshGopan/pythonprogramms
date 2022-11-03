class Person:       #parent class/super class/base class
    def __init__(self,name,age,place):
        self.n = name
        self.a =age
        self.p = place
    def printvalue(self):
        print(self.n,self.a,self.p)
f=open('persondata.txt','r')
for i in f:
    d=i.rstrip("\n").split(",")
    # print(d)
    name=d[0]
    age=d[1]
    place=d[2]
    p=Person(name,age,place)
    p.printvalue()
    print("......................")