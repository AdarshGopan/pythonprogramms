n1=10
n2=20
#swapping numbers
print("method 1")
print("before swapping n1 ",n1)
print("before swapping n2 ",n2)
temp=n1
n1=n2
n2=temp
print("after swapping n1 ",n1)
print("after swapping n2 ",n2)
#method 2
#tuple unpacking method
n1,n2=n2,n1
print("second method")
print("after swapping n1 ",n1)
print("after swapping n2 ",n2)
print("method 3")
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("after swapping n1 ",n1)
print("after swapping n2 ",n2)

