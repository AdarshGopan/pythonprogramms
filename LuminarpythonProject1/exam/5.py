f=open('fileexam.txt','r')
d={}
for i in f:
    s=i.rstrip('\n')
a=s.split(' ')
for i in a:
    if i not in d:
        d.update({i:1})
    else:
        v=d[i]
        v=v+1
        d.update({i:v})
print(d)
