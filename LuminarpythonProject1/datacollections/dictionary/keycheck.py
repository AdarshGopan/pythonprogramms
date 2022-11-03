d={0:10,2:20,3:30}#replace amal to anu
n=int(input("enter the number"))
if n in d.keys():                       #if we want keys with d.keys() and d .
    print("present")                     # we want values with d.values()
else:
    print("not present")


# for i in d:
#     if n==i:
#         print("present")
#         break
# else:
#     print("not present")