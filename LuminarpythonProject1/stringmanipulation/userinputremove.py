# n=input("enter the text")
# p=input("enter the letter to remove")
# m=""
# for i in n:
#     if i==p:
#         continue
#     m=m+i
# print(m)

n=input("enter the text")
p=input("enter the letter to remove")
m=""
for i in n:
    if i not in p:
        m=m+i
print(m)