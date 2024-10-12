import random
import sys
options = ["Rock", "Paper", "Scissor"]

print("Welcome to Stone Paper Scissor game")
print("Version 1 v 1 and AI")
print("Which mode do you want to play?")
print("1. Human VS Human")
print("2. Human VS AI")

user_mode = input("Enter the mode you want to play (1 or 2): ")

if user_mode == "2":
    print("You have chosen the mode Human VS AI")
    player_name = input("Enter your name: ")

    while True:
        ai_choice = random.choice(options)
        print("The options are: Rock, Paper, Scissor")
        player_choice = input(f"{player_name}, enter your option: ")

        if player_choice not in options:
            print("Invalid choice! Please choose between Rock, Paper, or Scissor.")
            continue

        print(f"The AI chose: {ai_choice}")

        if (player_choice == "Rock" and ai_choice == "Scissor") or \
           (player_choice == "Paper" and ai_choice == "Rock") or \
           (player_choice == "Scissor" and ai_choice == "Paper"):
            print(f"{player_name} won the game!")
        elif player_choice == ai_choice:
            print("It's a tie!")
        else:
            print("AI won the game!")

        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

elif user_mode == "1":
    print("You have chosen the mode Human VS Human")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    rounds = 4
    score1, score2 = 0, 0

    for round in range(1, rounds + 1):
        print(f"\nRound {round} Start!")
        print(f"{player1}, choose your option: 1. Rock  2. Paper  3. Scissor")
        choice1 = input(f"{player1}, enter your choice (1-3): ")
        choice1 = options[int(choice1) - 1]

        print(f"{player2}, choose your option: 1. Rock  2. Paper  3. Scissor")
        choice2 = input(f"{player2}, enter your choice (1-3): ")
        choice2 = options[int(choice2) - 1]

        if (choice1 == "Rock" and choice2 == "Scissor") or \
           (choice1 == "Paper" and choice2 == "Rock") or \
           (choice1 == "Scissor" and choice2 == "Paper"):
            score1 += 1
            print(f"{player1} won this round!")
        elif choice1 == choice2:
            print("It's a tie!")
        else:
            score2 += 1
            print(f"{player2} won this round!")

        print(f"{player1} Score: {score1}, {player2} Score: {score2}")

    print("\nGame Over!")
    if score1 > score2:
        print(f"{player1} is the overall winner!")
    elif score2 > score1:
        print(f"{player2} is the overall winner!")
    else:
        print("It's a tie!")

else:
    print("Invalid mode selected. Please restart the game.")
