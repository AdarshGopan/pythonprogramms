n1=float(input("enter 1st number"))
n2=float(input("enter 2nd number"))
n3=float(input("enter 3rd number"))
if n2>n1:
    if n2>n3:
        print("greatest number is n2=",n2)
    else:
        print("greatest number is n3=", n3)
elif n1==n2==n3:
    print("numbers are all equal")
else:
    if n1>n3:
        print("greatest number is n1=", n1)
    else:
        print("greatest number is n3=", n3)
