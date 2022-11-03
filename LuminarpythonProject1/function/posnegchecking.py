# def check():
#     n=int(input("enter the number"))
#     if n>0:                                #WITHOUT ARGUMENT
#         print(n,"number is positive")
#     elif n == 0:
#         print(n, "number is zero")
#     else:
#         print(n,"number is negative")
# check()

# def check(n):
#     if n>0:
#         print(n,"number is positive")
#     elif n==0:
#         print(n,"number is zero")           #WITH ARGUMENT
#     else:
#         print(n,"number is negative")
# a=int(input("enter the number"))
# check(a)

def check(n):
    if n>0:
        return "number is positive"
    elif n==0:
        return "number is zero"
    else:                                         #WITH ARGUMENT AND RETURN
        return "number is negative"
# a = int(input("enter the number"))
# b = check(a)
# print(b)
ch=input("you want to continue yes/no")
while ch=="yes" or ch=="YES":
    a = int(input("enter the number"))
    b=check(a)
    print(b)
    ch = input("you want to continue yes/no")


