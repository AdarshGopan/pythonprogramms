l=[1,88,5,9,66,45,-5,-3,77,0]
# l.sort()
# print(l)
m=[]
while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    m.append(min)
    l.remove(min)
print(m[-1])

