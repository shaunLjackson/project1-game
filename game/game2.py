import random
import csv
import math
from pymongo import MongoClient
import json

# opening the CSV file
with open('game.csv', mode = 'r') as file:
    # reading the csv file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)

def player_choice():
    while True:
        try:
            player1_choice = input("Enter a choice (rock, paper, scissors): ").strip()
            if not player1_choice == "rock" and not player1_choice == "paper" and not player1_choice == "scissors":
                raise ValueError
            elif  player1_choice == "":
                raise ValueError
            return player1_choice
        except ValueError:
            print("Oh No! invalid choice! Please choose rock, paper, or scissors")

def save_game_to_db(player1_score,computer_score):
    client = MongoClient()
    python_game = client.python_game
    games = python_game.games

    game_dict = {

    "winner" :  "player" if player1_score > computer_score else "computer",
    "player1_score" : player1_score,
    "computer_score" : computer_score

    }
    games.insert_one(game_dict)

def main():
    while True:

        while True:
            try:
                turns = int(input("\nBest of (3 or 5) games: "))
                if not (turns == 3 or turns == 5):
                    raise ValueError
                break            
                
            except ValueError:
                print("Invalid choice.")
        necessary_wins = int(math.ceil(turns/2))
        player1_wins = 0
        computer_wins =0

        while True:
            player1_choice = player_choice()
            computer_choice = computer_choice = random.choice(["rock", "paper", "scissors"])
            print("\nYou chose {0}, computer chose {1}.\n".format(player1_choice, computer_choice))
            if player1_choice == computer_choice:
                print("Both players selected {}. It's a tie!".format(player1_choice))
            elif player1_choice == "rock":
                if computer_choice == "scissors":
                    print("Rock smashes scissors! You win!")
                    player1_wins += 1
                else:
                    print("Paper covers rock! You lose.")
                    computer_wins += 1
            elif player1_choice == "paper":
                if computer_choice == "rock":
                    print("Paper over rock! You Win!")
                    player1_wins += 1
                else:
                    print("Scissors cuts thru paper! You lose.")
                    computer_wins += 1
            elif player1_choice == "scissors":
                if computer_choice == "paper":
                    print("Scissors cut thru paper! You Win!")
                else:
                    print("Rock smashes scissors! You lose.")
                    computer_wins += 1
            print("\n>>> SCORE: player:{} vs CPU:{} <<<".format(player1_wins,computer_wins))

            if player1_wins == necessary_wins:
                print("/n>>> You Win!! <<<")
                break
            elif computer_wins == necessary_wins:
                print("\n>>>> Computer wins!! <<<")
                break

        save_game_to_db(player1_wins, computer_wins)
        print("\n>>> You scored: {0} point(s) CPU scored: {1} point(s) <<<".format(player1_wins,computer_wins))

        play_again = input("\nWould you like to play again: 'y' for yes 'q' for quit: ")
            
        if play_again == 'q':
            break

    client = MongoClient()
    python_game = client.python_game
    games = python_game.games
    games.delete_many({})

    
if __name__=='__main__':
    main() 
