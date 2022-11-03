class Addition:
    def setvalue(self,num1,num2):
        self.n1=num1
        self.n2=num2
    def add(self):
        # s=n1+n2
        sum=self.n1+self.n2
        print("sum of it = ",sum)
a1=Addition()
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
a1.setvalue(n1,n2)
a1.add()