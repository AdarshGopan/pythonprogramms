f=open('file4.txt','r')
l=[]
for i in f:
    n=i.rstrip('\n').split(' ')
    l.extend(n)
print(l)