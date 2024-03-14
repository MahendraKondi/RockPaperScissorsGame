import random
print("Welcome to the game:)")
computer_wins = 0
user_wins = 0
options = ['paper','scissors','rock']
while True:
    user_input = input("Select one from rock/paper/scissors q for quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    com_choice = random.randint(0,2)
    com_pick = options[com_choice]
    if user_input == "rock" and com_pick == "scissors":
        print("You won!!")
        user_wins += 1
    elif user_input == "paper" and com_pick == "rock":
        print("You won")
        user_wins += 1
    elif user_input == "scissors" and com_pick == "paper":
        print("You won!!")
    else:
        print("You lost!!")
        computer_wins += 1

print("You won",user_wins,"times.")
print("Computer wins",computer_wins,"times.")