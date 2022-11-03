class Books:
    def printbook(self,n):
        self.n=n
        print("inside A =",self.n)
class chemistry(Books):
    def printbook(self,a):
        self.a=a
        print("inside chemistry book =",self.a)
class maths(Books):
    def printbook(self,c):
        self.c=c
        print("inside maths book=",self.c)
m=maths()
m.printbook("maths")

c=chemistry()
c.printbook("chemistry ")