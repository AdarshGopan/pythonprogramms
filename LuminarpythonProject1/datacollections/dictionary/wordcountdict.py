s=input("enter the words")
a=s.split(' ')
print(a)
d={}
for i in a:
    if i not in d:
        d.update({i:1})
    else:
        v=d[i]
        v=v+1
        d.update({i:v})
print(d)
