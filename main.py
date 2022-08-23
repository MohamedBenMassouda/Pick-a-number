import random

player_choice = int(input("Choose a number between 1 and 100:"))
while 1 > player_choice > 100 :
    player_choice = int(input("Choose a number between 1 and 100:"))

comp_choice = random.randint(1, 100)

if player_choice == comp_choice:
    print("We knew it is ", player_choice)

elif player_choice < comp_choice:
    print("The computer guessed it wrong, but it has another guess.")
    print("The computer guessed", comp_choice)

    comp_choice2 = random.randint(1, 100)
    while comp_choice2 == comp_choice:
        comp_choice2 = random.randint(1, 100)

    if player_choice == comp_choice2:
        print("We knew it is ", player_choice)
    else:
        print("The computer guessed it wrong twice you won")
        print("The computer guessed", comp_choice2)

