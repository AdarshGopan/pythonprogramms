# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return(f)                                            #WITH ARGUMENT AND RETURN
# o = int(input("enter the number"))
# b=fact(o)
# print("sum",b)

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i                                            #WITH ARGUMENT
#     print(f)
# o = int(input("enter the number"))
# fact(o)

def fact():
    o = int(input("enter the number"))
    f=1                                                   #WITHOUT ARGUMENT
    for i in range(1,o+1):
        f=f*i
    print(f)
fact()