s={12,257,84,95,55,99,288,9,1,3,6,0}
print("orginal set=  ",s)
even=set()
odd=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("even set=",even)
print("odd set=",odd)