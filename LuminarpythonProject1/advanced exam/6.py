class Student:
    def __init__(self,name,roll,dept,mark):
        self.r=roll
        self.n = name
        self.d = dept
        self.m = mark
        # self.c = college_name
    def printvalue(self):
        print(self.n)
        print(self.r)
        print(self.d)
        print(self.m)
f=open("details.txt",'r')
l=[]
for i in f:
    d=i.rstrip("\n").split(',')
    # print(d)
    name=d[0]
    roll=d[1]
    dept=d[2]
    mark=d[3]
    s = Student(name,roll,dept,mark)
    l.append(int(s.m))
    s.printvalue()
    print(".................")
print(max(l)    )