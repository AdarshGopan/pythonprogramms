def fun() -> object:
    n = int(input("enter 1 number"))
    m = int(input("enter 2 number"))
    s = n + m
    print(s)
    return s
a=fun()
b=fun()
s=int(a+b)
print("sum of sum",s)
