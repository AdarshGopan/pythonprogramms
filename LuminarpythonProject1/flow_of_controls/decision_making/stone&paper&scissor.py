import random
player1 = input("  Select your choice from (rock, Paper, pencil, scissor) :")
player2 = random.choice(["pencil", "rock", "scissor","paper"])
print("  you   select : ",player1)
print("  computer select : ", player2)
if player1 == "rock" and player2 == "paper":
    print("  Computer Won")
elif  player1 == "paper" and player2 == "scissor":
     print("  Computer Won")
elif player1 == "scissor" and player2 == "rock":
     print("  Computer Won")
elif player2 == "pencil" and player1 == "paper":
    print("  Computer Won")
elif  player1 == "pencil" and player2 == "scissor":
     print("  Computer Won")
elif player1 == "pencil" and player2 == "rock":
     print("  Computer Won")
elif player2 == "rock" and player1 == "paper":
    print("  You Won")
elif  player2 == "paper" and player1 == "scissor":
     print("  You Won")
elif player2 == "scissor" and player1 == "rock":
     print("  You Won")
elif player2 == "rock" and player1 == "pencil":
    print("  Computer Won")
elif  player2 == "paper" and player1 == "pencil":
     print("  You Won")
elif player2 == "scissor" and player1 == "pencil":
     print("  Computer Won")
elif player1 == player2:
     print("  TIE")
else:
	 print("You Won")