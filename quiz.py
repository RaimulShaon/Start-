print ("Welcome to my computer quiz!")

game= input("do you want to play game? Y/NO: ").upper()
if game != "Y":
    quit()

print("let's play!")
score = 0

anser = input("what is ur name? ").upper()
if anser == "ANSWER":
    print(" R8 Anser!")
    score += 1
    print("Next QSN...")
else:
    print("....Wrong ANS...")
    print("Game Over!!!")

anser = input("what is ur name? ")
if anser == "ANSWER":
    print(" R8 Anser!")
    score += 1
    print("Next QSN...")
else:
    print("....Wrong ANS...")
    print("Game Over!!!")

anser = input("what is ur name? ")
if anser == "ANSWER":
    print(" R8 Anser!")
    print("Next QSN...")
else:
    print("....Wrong ANS...")
    print("Game Over!!!")


print("Your Total Score is: " + str(score))