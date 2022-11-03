def prime(init,fin):
    sum=0
    for i in range(init, fin + 1):
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            sum=sum+i
            #print(i, end=",")
    return sum
init=int(input("enter the initial range"))
fin=int(input("enter the final range"))
print("prime numbers sum",end=":")
s=prime(init,fin)
print(s)