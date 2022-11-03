k=7
for i in range(5):
    for a in range(k):
        print(end=" ")
    k-=1
    for j in range(i):
        if i==3 and j==1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()