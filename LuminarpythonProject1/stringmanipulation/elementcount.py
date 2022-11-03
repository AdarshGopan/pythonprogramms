s1="adarshafshgdhghctdhgchgtaa"
u=input("enter letter")
count=0
for i in s1:
       if u==i:
              print(u)
              count+=1
else:
       print("entered letter is not present")

print("entered letter in word =",count)
