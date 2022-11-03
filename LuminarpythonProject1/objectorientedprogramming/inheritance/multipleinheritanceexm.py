class Mark:
    def setmark(self,sub1,sub2,sub3,sub4,sub5):
        self.s1=sub1
        self.s2=sub2
        self.s3=sub3
        self.s4=sub4
        self.s5=sub5
class Sports:
    def setSportsmark(self,Grace):
        self.Grace=Grace
class Student(Mark,Sports):
    def setStudent(self,name,place,age,phno):
        self.n=name
        self.p=place
        self.a=age
        self.phno=phno
    def details(self):
        print("name of student:",self.n)
        print("place of student:",self.p)
        print("age of student:",self.a)
        print("phno of student:",self.phno)
        tot=self.s1+self.s2+self.s3+self.s4+self.s5
        print("theory mark of student:",tot)
        print("Grace mark of student:",self.Grace)
        print("Total mark of student:",tot+self.Grace)
opt="yes"
while True:
    if opt=="no" or opt=="NO":
        break
    elif opt=="yes" or opt=="YES":
        n=int(input("enter the limited to create instance"))
        for i in range(n):
            si=Student()
            n = input("enter your name")
            p = input("enter your place")
            a = int(input("enter your age"))
            ph = int(input("enter your phone number"))
            si.setStudent(n, p, a, ph)
            m1 = int(input("enter your marks"))
            m2 = int(input("\n"))
            m3 = int(input("\n"))
            m4 = int(input("\n"))
            m5 = int(input("\n"))
            si.setmark(m1,m2,m3,m4,m5)
            g=int(input("enter your grace mark"))
            si.setSportsmark(g)
            si.details()
    else:
        print("invalid")
    opt=input("Do you want to continue")
