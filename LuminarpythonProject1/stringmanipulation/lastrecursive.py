 n=input("enter the string")
m =""
k =""
for i in n:
    if i not in m:
        m=m+i
    elif i not in k:
        k=k+i
        print(k)
print("first repeat value is=",k[0])
print("second repeat value is=",k[1])
print("second last repeat value is=",k[-2])
print("last repeat value is=",k[-1])