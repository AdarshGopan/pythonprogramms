k=7
for i in range(5):
    for a in range(k):
        print(end=" ")
    k-=1
    for j in range(i):
        print("*",end=" ")
    print()