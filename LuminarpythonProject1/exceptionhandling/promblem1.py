n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
r=n1-n2
if r<0:
    raise Exception("negative number")
else:
    print(r)