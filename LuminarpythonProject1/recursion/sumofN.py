def findsum(n):
    if n==0:
        return 0
    else:
        print(n,end=",")
        return n+findsum(n-1)
n=int(input("enter the number"))
print(" sum of n natural numbers=",findsum(n))