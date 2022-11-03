# list comprehension
l=[2,1,7,4,5,8,6,3,5,345]
# c=[]
# for i in l:
#     c.append(i**3)
# print(c)

# c=[i**3 for i in l]
# print(c)

even=[i for i in l if i%2==0]
odd=[i for i in l if i%2!=0]
print(even)
print(odd)

