import random

def roll():
    min_value = 1
    max_value = 6
    rol = random.randint(min_value, max_value)

    return rol

while True:
    players = input("Enter player Num (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print('Must be 2 to 4.')

    else:
        print('invalid Input.')

target = 20
player_score = [0 for _ in range(players)]

print(player_score)

# Main game loop
game_over = False

while max(player_score) < target:
    for plyer_num in range(players):
        print(" Player ", plyer_num +1, 'turn has jst started \n' )
        print("Your total score is: ", player_score[plyer_num],"\n")
        current_score = 0

        while True:
            lets_roll = input('Lets Roll...(y) ')
            if lets_roll != "y":
                break

            value = roll()
            if value == 1:
                print('you roll a 1! ')
                current_score = 0
                break
            else:
                current_score += value
                print("roll again:", value)

            print("your score is:", current_score)

        player_score[plyer_num] += current_score
        print('your total score: ', player_score[plyer_num])

        if player_score[plyer_num] == target or player_score[plyer_num] >= target :
            game_over = True
            break


max_score = max(player_score)
winner = player_score.index(max_score)
print("Winner is:",winner+1, '& MAX SCORE IS: ',max_score)
print(f' Players score {player_score}')
print('Game Over')
