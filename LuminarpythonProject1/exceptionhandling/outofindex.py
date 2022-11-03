# l=[1,2,3,4,5,6,9]
# i=int(input("enter the index to get element"))
# try:
#     print(l[i])
# except:
#     print("index must be in the range",len(l)-1)

l=[1,2,3,4,5,6,9]
i=int(input("enter the index to get element"))
try:
    print(l[i])
except Exception as c:
    print(c)