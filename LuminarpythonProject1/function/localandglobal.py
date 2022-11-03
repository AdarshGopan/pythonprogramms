x=9
print(x)
def printx():
    global x
    x=10
    x-=1
    print(x)
printx()
print(x)