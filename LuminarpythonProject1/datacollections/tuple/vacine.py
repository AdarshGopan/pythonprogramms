  v=[('prasad',99),('renju',99),('shammi',76),('sanju',35),('sanjana',56)]
age=[]
for i in v:
    age.append(i[1])
#print(age)
max=max(age)
#print(max)
for j in v:
    if j[1]==max:
        print(j[0],"is the person who vaccinate first")
        break