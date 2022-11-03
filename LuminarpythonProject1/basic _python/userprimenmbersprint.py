init=int(input("enter the initial range"))
fin=int(input("enter the final range"))
print("prime numbers",end=":")
for i in range(init,fin+1):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i,end=",")