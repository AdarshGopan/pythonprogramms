s1={12,33,3,6,4,8,9,12.5,22,9,65.9,44.9,False}
s2={33,6,9,23,False,7,1,88.4,22.9,65.9,33.8}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i) # print(i)
print("common elements=",s3)
