import random

opposites = {
    "paper": "rock",
    "rock": "scissors",
    "scissors": "paper"
}


def main():
    player_count = 0
    enemy_count = 0
    while True:
        enemy_options = ["rock", "paper", "scissors"]
        enemy = random.choice(enemy_options)

        player_answer = input("chose, rock, paper or scissors: ")
        print(f"The enemy chose {enemy}")
        if opposites.get(player_answer) == enemy:
            player_count += 1
            print(f"You earned a point, now you have {player_count} points.")
        elif opposites.get(enemy) == player_answer:
            enemy_count += 1
            print(f"You lost, the enemy have {enemy_count} points.")
        else:
            print("tie.")
        print(" ")

        if enemy_count == 3:
            print("you lost!")
            break
        elif player_count == 3:
            print("you won!")
            break


if __name__ == "__main__":
    main()
