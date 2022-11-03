n=int(input("Enter the number to get factorial:"))
fact=1
while n>0:
    fact*=n
    n-=1
print("Enetered number factorial is =",fact)