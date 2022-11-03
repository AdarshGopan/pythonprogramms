f=open('file1.txt','r')
# print(f)
for i in f:
    a=i.rstrip("\n")
    print(a)