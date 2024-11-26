name= input("Enter your name: ")
print("Welcome", name, "to this exciting adventure!")

answer= input("You have reached the end of the road. You have a choice to go left or right. Where would you like to go? ").lower()

if answer == "left":
    answer= input("You come to a river, you can walk around it, or you can swim across. Type walk to walk around or swim to swim around. ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")






elif answer == "right":
    answer= input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()

    if answer == "cross":
        answer= input("You made it across the bridge. Now you saw a fairy. A red fairy and a blue fairy. It asked you to choose between them. Who would you pick? (red/blue) ").lower()
        if answer == "red":
            print("You were taken away by the evil red fairy. GAME OVER")
        elif answer == "blue":
            print("You found the fairy of life. CONGRATULATIONS you WON the GAME!")
        else:
            print("Not a valid option. You lost.")


    elif answer == "back":
        print("You went back to the main road. And got into an accident. You lost")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")



print("Thank you for trying the game", name, "!")
