class A:
    def printA(self,num1):
        self.num1=num1
        print("In A class",self.num1)
class B:
    def printB(self):
        print("In B class",self.num1)
class C(A,B):      #multiple class(A,B) inherited by Class C
    def printC(self):
        print("In C class",self.num1)
c=C()
c.printA(9)
c.printB()
c.printC()