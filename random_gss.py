import random

top_of_range = input("enter a Num: ")
guss = 0



if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print(" pls enter above num of 0")




ran = random.randint(1,top_of_range)

while True:
    guss += 1
    user_gss = input("Make a GUESS: ")
    if user_gss.isdigit():
        user_gss = int(user_gss)
    else:
        print("type a num next time. ")
        continue

    if user_gss == ran:
        print(" You got the R8 Num!!")
        break

    else:
        print("you got the wrng NUM")

print( 'Total guss ', guss, "guss")
