import random

#random_number= random.randrange(-1, 10) #numbers between -1 to 9 not including 10
# random.randint(-1, 10) all numbers within range but including 10

top_range= input("Enter a number as the top range: ")

if top_range.isdigit():
    top_range= int(top_range)

    if top_range <0:
        print("Please type a number larger than 0")
        quit()
else:
        print("Please type a number next time")



random_number= random.randint(0, top_range)
attempt= 0

while True:
    attempt += 1
    user_guess= input("Make a guess: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("Bullseye! You got it.")
        break
    elif user_guess<random_number:
        print("Higher")
    elif user_guess>random_number:
        print("Lower")

print("You got it in ", attempt, "guesses")
