l = [12, 43, 23, 2434, 3543, 22, 245, 62, 74, 2, 8, 9, 6, 4, 63, 10, 787, 65, 0, 41, 49, 3]
l.sort()
print(l)
def binary_search(l,x,i,j):
    if j>=i:
        mid=i+(j-i)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binary_search(l,x,i,mid-1)
        else:
            return binary_search(l,x,mid+1,j)
    else:
        return -1
x=int(input("enter the element to search"))
i=0
j=len(l)-1
r=binary_search(l,x,i,j)
if r!= -1:
    print("search element",x,"at index of",r)
else:
    print("element not found")