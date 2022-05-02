import random
import csv


# opening the CSV file
with open('game.csv', mode = 'r') as file:
    # reading the csv file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)




while True:
    try:
        player1_choice = input("Enter a choice (rock, paper, scissors): ").strip()
        if not player1_choice == "rock" and not player1_choice == "paper" and not player1_choice == "scissors":
        
            raise ValueError
        elif  player1_choice == "":
            raise ValueError 
        break         


    except ValueError:
        print("Oh No! invalid choice! Please choose rock, paper, or scissors")


computer_choice = random.choice(["rock", "paper", "scissors"])
print("\nYou chose {0}, computer chose {1}.\n".format(player1_choice, computer_choice))

if player1_choice == computer_choice:
    print("Both players selected {}. It's a tie!".format(player1_choice))
elif player1_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
        
    else:
        print("Paper covers rock! You lose.")
        
elif player1_choice == "paper":
    if computer_choice == "rock":
        print("Paper over rock! You Win!")
        
    else:
        print("Scissors cuts thru paper! You lose.")
        
elif player1_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cut thru paper! You Win!")
    else:
        print("Rock smashes scissors! You lose.")
       



   