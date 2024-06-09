import  random

User_wins = 0
ai_wins = 0

option = ["Rock", "Paper", "Scissor"]
time = 1
while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ")
    if user_input == 'Q':
        break
    if user_input not in option:
        continue

    random_num = random.randint(0,2)

    computer = option[random_num]
    print("computer pick", computer + ".")

    if user_input == "Rock" and computer == "Scissor":
        print("YOU WIN!!")
        User_wins += 1

    elif user_input == "Paper" and computer == "Rock":
        print("YOU WIN!!")
        User_wins += 1

    elif user_input == "Scissor" and computer == "Paper":
        print("YOU WIN!!")
        User_wins += 1

    elif user_input == computer:
        print("RESTART")


    else:
        print("YOU LOSE!!!")
        ai_wins += 1

print("Your Point", + User_wins)
print("COM", + ai_wins)
print("****Game Over****")
