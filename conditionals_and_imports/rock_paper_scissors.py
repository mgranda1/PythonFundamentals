# Rock paper scissors game
import random

# Roll the dice
roll = random.randint(1,6)
guess = int(input("Guess the dice roll: "))
if guess == roll:
    print('You guessed the roll correctly. Good gambling')
else:
    print('Computer rolled: ' + str(roll))

choices_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices_list)
user_choice = input("\nDo you want rock paper or scissors? ")
print('Computer rolled ' + computer_choice + ' and you rolled ' + user_choice)

if computer_choice == user_choice:
    print ('It\'s a Tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You Win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You Win')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You Win')
else:
    print('You lose.')