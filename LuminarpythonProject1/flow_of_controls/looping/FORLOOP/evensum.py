init=int(input("enter initial range "))
fin=int(input("enter final range"))
sum=0
print("even numbers  between range is=",end="")
for i in range(init,fin+1):
    if i%2==0:
        sum=sum+i
        print(i,end=",")
print("")
print("even numbers sum between range is=",sum)