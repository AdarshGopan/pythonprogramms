for i in range(1,6):
    print(end="")
    for a in range(i):
        print("1",end=" ")
    print("\r")
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("2", end=" ")
    print("\r")
print(end="")
for i in range(1,6):
    print(end="")
    for a in range(i):
        print("3",end=" ")
    print("\r")
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("4", end=" ")
    print("\r")