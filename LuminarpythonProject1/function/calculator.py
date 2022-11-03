def add(n1,n2):
    print(n1,"+",n2,"=",n1+n2)
def sub(n1,n2):
    print(n1,"-",n2,"=",n1-n2)
def mul(n1,n2):
    print(n1,"*",n2,"=",n1*n2)
def div(n1,n2):
    print(n1,"/",n2,"=",n1/n2)
while True:
    n=input("CHOOSE YOUR CHOICE\n+.ADDITION\n-.SUBSTRATION\n*.MULTIPLICATION\n/.DIVISION\nSTOP\n")
    if n=="stop" or n=="STOP":
        print("STOPPED")
        break
    elif n=="+" or n=="-" or n=="*" or n=="/":
        n1=float(input("enter 1st number"))
        n2=float(input("enter 2nd number"))
        if n=="+":
            add(n1,n2)
        elif n=="-":
            sub(n1,n2)
        elif n=="*":
            mul(n1,n2)
        elif n=="/":
            div(n1,n2)
    else:
        print("wrong input")