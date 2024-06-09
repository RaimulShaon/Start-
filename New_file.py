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
        if 2 <= players <= 4:
            break
        else:
            print('Must be 2 to 4.')
    else:
        print('Invalid Input.')

target = 20
player_score = [0 for _ in range(players)]

print(player_score)

# Main game loop
game_over = False

while not game_over:
    for player_num in range(players):
        print(f"Player {player_num + 1} turn has just started\n")
        print(f"Your total score is: {player_score[player_num]}\n")
        current_score = 0

        while True:
            lets_roll = input('Lets Roll...(y) ')
            if lets_roll != "y":
                break

            value = roll()
            if value == 1:
                print('You rolled a 1!')
                current_score = 0
                break
            else:
                current_score += value
                print(f"Roll again: {value}")

            print(f"Your score is: {current_score}")

        player_score[player_num] += current_score
        print(f"Your total score: {player_score[player_num]}")

        if player_score[player_num] >= target:
            game_over = True
            break

max_score = max(player_score)
winner = player_score.index(max_score) + 1
print(f"Winner is: Player {winner} with a score of {max_score}")
print(f' Players score {player_score}')
print('Game over')
