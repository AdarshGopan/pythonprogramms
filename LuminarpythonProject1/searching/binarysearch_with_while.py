l = [12, 43, 23, 2434, 3543, 22, 245, 62, 74, 2, 8, 9, 6, 4, 63, 10, 787, 65, 0, 41, 49, 3]
l.sort()
print(l)
x=int(input("enter the element to search"))
flag=0
i=0
j=len(l)-1
while i<=j:
    mid=(i+j)//2
    if x<l[mid]:
        j=mid-1
    elif x>l[mid]:
        i=mid+1
    else:
        flag=1
        break
if flag==1:
    print("element at the index ",mid)
else:
    print("element not present")