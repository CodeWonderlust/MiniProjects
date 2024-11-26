import random

user_wins= 0
comp_wins= 0


options= ["rock", "scissors", "paper"]

while True:
    user_input= input("Type Rock/Scissors/ Paper or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "scissors", "paper"]: #list
        continue

    random_number = random.randint(0, 2)  #radint is a function rand int 0, 1, and 2
        # rock 0  # scissors 1      # paper 2
    computer_pick= options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost")
        comp_wins += 1


print("You won", user_wins, "times")
print("Computer won", comp_wins, "times")
print("Goodbye!")
