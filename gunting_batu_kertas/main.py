from random import randint

#create a list of play options
t = ["Batu", "Kertas", "Gunting"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Batu, Kertas, Gunting?")
    if player == computer:
        print("Tie!")
    elif player == "Batu":
        if computer == "Kertas":
            print("Kamu Kalah", computer, "covers", player)
        else:
            print("Kamu Menang", player, "smashes", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print("Kamu Kalah, computer, "cut", player)
        else:
            print("Kamu Menang", player, "covers", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Kamu Kalah", computer, "smashes", player)
        else:
            print("Kamu Menang", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
