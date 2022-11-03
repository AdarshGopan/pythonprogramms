# n=int(input("ENTER THE SIZE OF STACK"))
# l=[]
# while True:
#     op=input("CHOOSE YOUR CHOICE\n 1.PUSH \n 2.POP \n 3.TO STOP\n")
#     if op == '3':
#         break
#     elif op == '1':
#         if len(l)==n:
#             print("ALERT !!!!! STACK OVERFLOW")
#         else:
#             a=input("ENTER YOUR ELEMENT TO PUSH")
#             l.append(a)
#             print("AFTER PUSH =",l)
#     elif op == '2':
#         if len(l)==0:
#             print('ALERT !!!!! STACK UNDERFLOW')
#         else:
#             l.remove(l[-1])
#             print("AFTER POP = ",l)
#     else:
#         print("WRONG INPUT")

stack=[]
size=int(input("enter the size"))
c=0
def push():
    global c
    if c>=size:
        print("stack overflow")
    else:
        n=int(input("enter the element to push"))
        stack.append(n)
        c+=1
        print(stack)
def pop():
    global c
    if c==0:
        print("stack is underflow")
    else:
        stack.pop()
        print(stack)
        c-=1
while True:
    opt=int(input("select your option\n 1.push\n 2.pop \n 3.stop"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        break
    else:
        print("invalid input")



























