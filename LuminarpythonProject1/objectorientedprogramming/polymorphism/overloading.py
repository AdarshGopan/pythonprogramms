# polymorphism   ........many form
#methods

# method overloading
# method over-riding
# overloading ...same method name diff num of argument
class A:
    def printA(self,n):
        self.n=n
        print("inside A=",self.n)
class B(A):
    def printA(self):
        print("inside B")
b=B()
b.printA()
b.printA()