f=open('numbers.txt','r')
p=open('validnumbers.txt','w')
for i in f:
    n=i.rstrip('\n')
    if len(n)==10:
        p.write(i)
