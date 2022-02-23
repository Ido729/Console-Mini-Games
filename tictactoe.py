import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

taken_places = []
game_running = True
win_possibles = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
type = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def player():
    global type
    if type == "X":
        position = int(input(f"Chose the position from 1-9 for the {type}: ")) - 1
        if position in taken_places:
            print("This position is already taken")
        else:
            board[position] = type
            taken_places.append(position)
            type = "O"


def enemy():
    global type
    numbers = list(range(0, 9))
    for num in taken_places:
        numbers.remove(num)
    enemy_position = random.choice(numbers)
    board[enemy_position] = type
    taken_places.append(enemy_position)
    type = "X"


def result():
    global game_running
    for winner_sequence in win_possibles:
        if board[winner_sequence[0]] == board[winner_sequence[1]] and board[winner_sequence[0]] == board[
            winner_sequence[2]] and board[winner_sequence[0]] != "-":
            print("game over")
            game_running = False
            return board[winner_sequence[0]]
    if len(taken_places) == 9:
        print("tie")
        game_running = False


def main():
    player()
    display_board()
    result()
    enemy()
    display_board()
    result()


while game_running:
    main()
