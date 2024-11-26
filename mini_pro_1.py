print("Welcome to my world: QUIZ GAME!")

playing= input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's go!")

score= 0

answer1= input("What does CPU stands for? ")
if answer1.lower() == "central processing unit":
    print("Correct")
    score += 1 #its like saying score= score+1 take the value of score and add 1
else:
    print("Incorrect")
answer1= input("What does JPN stands for? ")
if answer1.lower() == "japan":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer1= input("What does <3? ")
if answer1.lower() == "love":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer1= input("What does Php mean? ")
if answer1.lower() == "philippines":
    print("Correct")
    score += 1
else:
    print("Incorrect")


print("You got " + str(score)+ " questions correct")
# make the score to string because it will add the YOU GOT to the score
print("You got " + str((score / 4) * 100) +"%")
