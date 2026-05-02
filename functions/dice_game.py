# Introducing functions and random module
import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()
    
    print(f"Player {player1} rolled {roll1}")
    print(f"Player {player2} rolled {roll2}")

    if roll1 == roll2:
        print("It's a TIE")
    elif roll1 > roll2:
        print(f"Player {player1} won!")
    else: 
        print(f"Player {player2} won!")


main()
