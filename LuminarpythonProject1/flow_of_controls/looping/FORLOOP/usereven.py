init=int(input("enter initial range "))
fin=int(input("enter final range"))
for i in range(init,fin+1):
    if i%2==0:
        print("even numbers between range is=",i)
