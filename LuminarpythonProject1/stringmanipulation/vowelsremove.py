n=input("enter the text")
m=""
for i in n:
    if i not in 'aeiou':
        m=m+i
print(m)