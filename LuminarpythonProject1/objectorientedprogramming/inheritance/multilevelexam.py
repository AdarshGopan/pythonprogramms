class A:
    def printA(this, num1):
        this.num1 = num1
        print("In A class", this.num1)


class B(A):
    def printB(this):
        print("In B class", this.num1)


class C(B):  # multiple class(A,B) inherited by Class C
    def printC(this):
        print("In C class", this.num1)


c = C()
c.printA(9)
c.printB()
c.printC()
