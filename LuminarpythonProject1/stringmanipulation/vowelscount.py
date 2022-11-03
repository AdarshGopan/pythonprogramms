str=input("enter any string")
s="aeiou"
count=0
for i in str:
    if i in s:
        count+=1
print("count=",count)