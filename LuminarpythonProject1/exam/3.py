student=[('anu',67),('amar',69),('arun',65)]
mark=[]
for i in student:
    mark.append(i[1])
print(mark)
maxmark=max(mark)
for i in student:
    if i[1]==maxmark:
        print("maximum mark got",i[0])