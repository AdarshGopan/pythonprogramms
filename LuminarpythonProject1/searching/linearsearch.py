def linear_search(x):
    for i in l:
        if i==x:
            print(l.index(i),"is index of searched element",i)
            break
    else:
        print("your element not present")
l = [12, 43, 23, 2434, 3543, 22, 245, 6, 74, 2, 8, 9, 6, 4, 6, 0, 787, 65, 4, 4, 4, 3]
x = int(input("enter the element you want to search"))
linear_search(x)