import random


def main():
    print("The first to reach 3 points win.")
    enemy_count = 0
    player_count = 0
    while True:
        if player_count == 3:
            print("You won!")
            break
        elif enemy_count == 3:
            print("You lost!")
            break

        enemy_rolling = random.randint(1, 6)
        player_rolling = random.randint(1, 6)
        submit_request = input('Type "roll" to rolling the dice: ')
        if submit_request == "roll":
            print(f"You got {player_rolling}")
            print(f"The enemy got {enemy_rolling}")
        else:
            print('You didnt typed "roll" right, start again.')
            break

        if bool(player_rolling > enemy_rolling):
            player_count += 1
            print(f"You have {player_count} point, while the enemy has {enemy_count} points.")
            print(" ")
        elif bool(enemy_rolling > player_rolling):
            enemy_count += 1
            print(f"The enemy has {enemy_count} point, while you have {player_count} points.")
            print(" ")
        else:
            print("tie, role again")
            print(" ")


if __name__ == "__main__":
    main()
