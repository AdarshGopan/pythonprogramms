n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
try:
    print("in try block")
    print(n1,"/",n2,"=",n1/n2)
except Exception as e:
    print(e)
finally:
    print('hello user')