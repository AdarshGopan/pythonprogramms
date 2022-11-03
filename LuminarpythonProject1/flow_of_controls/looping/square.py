init=int(input("enter initial range "))
fin=int(input("enter final range"))
for i in range(init,fin+1):
    if i%2==1:
        print("  square value of odd number",i,"(between range) is =",i**2)