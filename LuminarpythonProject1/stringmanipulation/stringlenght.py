s=input("enter the text")
count=0
for i in s:
    count+=1
print("length is",count)
print("inbuild length calculate",s.__len__())
print("inbuild length calculate",len(s))