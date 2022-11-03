#FIBANOCCI FUNC WITH ARGUMENT
def fibanocci(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        print(n1,end=",")
        t=n1
        n1=n2
        n2=t+n2
n=int(input("enter the range"))
fibanocci(n)