  queue=[]
size=int(input("enter the size"))
c=0
def enqueue():
    global c
    if c>=size:
        print("queue is full")
    else:
        n=int(input("enter the element to insert"))
        queue.append(n)
        c+=1
        print("after the enqueue stack =",queue)
def dequeue():
    global c
    if c==0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        print("after the dequeue the stack =",queue)
        c-=1
while True:
    opt=int(input("select your option\n 1.enqueue\n 2.dequeue \n 3.stop"))
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    elif opt==3:
        print("PROGRAM STOPPED")
        break
    else:
        print("invalid input")
