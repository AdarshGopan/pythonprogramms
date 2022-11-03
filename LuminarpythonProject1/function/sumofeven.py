#RANGE EVEN SUM FUNC WITH ARGUMENT RETURN
def evensum(n,f):
    sum=0
    for i in range(init,fin):
        if i%2==0:
            print("even numbers",i)
            sum=sum+i
    return (sum)
init=int(input("enter the initial range"))
fin=int(input("enter the final range"))
s=evensum(init,fin)
print("sum of even no btw the range",s)