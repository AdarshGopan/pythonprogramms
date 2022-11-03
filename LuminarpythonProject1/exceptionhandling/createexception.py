n=int(input("enter your number"))
if n<0:
    raise Exception("negative value")
else:
    print(n)