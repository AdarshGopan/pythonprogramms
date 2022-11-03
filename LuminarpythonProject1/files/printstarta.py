f=open('name.txt','r')
print("word start with a is given below")
for i in f:
    if i[0]=='a':
        d=i.rstrip('\n')
        print(d)