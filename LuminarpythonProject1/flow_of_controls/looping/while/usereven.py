init=int(input("enter initial range "))
fin=int(input("enter final range"))
sum=0
while init<=fin:
    if init%2==0:
        print("even numbers between range is=",init)
        sum+=init
    init+=1
print("sum of even numbers is =",sum)