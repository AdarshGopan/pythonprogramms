import random
player=random.choice(["1L","2L","3L","4L","5L","6L","7L"])
computer=random.choice(["1L","2L","3L","4L","5L","6L","7L"])
# print(player)
# print(computer)
for i in player:
    for j in computer:
        if i[0]<j[0]:
            print("computer win")
            break
        elif i[0]>j[0]:
            print("you win")
            break
        else:
            print("tie")
            break
