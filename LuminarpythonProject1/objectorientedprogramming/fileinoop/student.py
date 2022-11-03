class Student:
    def __init__(self,name,dept,mark):
        self.n = name
        self.d = dept
        self.m = mark
        # self.c = college_name
    def printvalue(self):
        print(self.n)
        print(self.d)
        print(self.m)
f=open("studentdata.txt",'r')
l=[]
for i in f:
    d=i.rstrip("\n").split(',')
    # print(d)
    name=d[0]
    dept=d[1]
    mark=d[2]
    s = Student(name, dept, mark)
    l.append(int(s.m))
    s.printvalue()
    print(".................")
print(max(l)    )



