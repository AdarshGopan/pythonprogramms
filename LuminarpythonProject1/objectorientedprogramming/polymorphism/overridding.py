# overriding ....same method name and same number of argumnt but child class method is invoke
class A:
    def printA(self,n):
        self.n=n
        print("inside A =",self.n)
class B(A):
    def printA(self,a):
        self.a=a
        print("inside B =",self.a)
b1=B()
b1.printA(3)
# b1.printA(7)
# b1=A()
# b1.printA(8)