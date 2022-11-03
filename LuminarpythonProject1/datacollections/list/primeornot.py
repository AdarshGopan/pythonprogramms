l=[1,2,3,4,5,6,7,8,9,10,11]
#print(len(l))
p=[]
nop=[]
for i in l:
    for a in range(2,i):
        if i%a==0:
            nop.append(i)
            break
    else:
        p.append(i)
print(p)
print(nop)
