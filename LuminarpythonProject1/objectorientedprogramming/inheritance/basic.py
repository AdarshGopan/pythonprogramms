class A:
    def printA(self,num1):
        self.num1=num1
        print("In A class")
class B(A):
    def printB(self):
        print("In B class",self.num1)
b=B()
b.printA(9)
b.printB()
