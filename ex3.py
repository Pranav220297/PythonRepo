while(1):
  c = int(input(" 1. To Play  2. To continue  3. To exit "))
  if  c==1 or c==2 :
    print("rock, paper or scissor")

    player_A = input("SELECT any for A ")
    player_B = input("SELECT any for B ")

    if player_A == player_B:
        print("Its a TIE")

    elif player_A == "rock":
        if player_B == "paper":
            print("B wins")
        else :
            print("A wins")

    elif player_A == "paper":
        if player_B == "scissor":
            print("B wins")
        else :
            print("A wins")

    elif player_A == "scissor":
        if player_B == "rock":
            print("B wins")
        else :
            print("A wins")
 

  else: 
      print("GAME OVER")
      break;