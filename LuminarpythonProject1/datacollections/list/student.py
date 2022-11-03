list=[['arun',334],['adarsh',765],['anjali',567],['vikram',645],['prasad',700]]
n=input("enter your name to get mark")
for i in list:
    if i[0]==n:
        print("your mark is", i[1])            # for a in i:
        break                                       #     if a==n:
else:
    print("wrong username")
