init=int(input("initial range"))
fin=int(input('final range'))
even=[i for i in range(init,fin+1) if i%2==0]
odd=[i for i in range(init,fin+1) if i%2!=0]
print(even)
print(odd)
