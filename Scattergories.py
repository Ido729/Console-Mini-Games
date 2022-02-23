import string
import random


class objects:
    def __init__(self):
        self.letters = string.ascii_uppercase
        self.chosen_letter = random.choice(self.letters)
        self.subjects_list = ['city', 'movie', 'animal', 'Game', 'country',
                              'Name', 'Sport', 'Food', 'Carton', 'Hobbies']
        self.subjects = random.sample(self.subjects_list, k=5)
        self.used = []
        print(f"The chosen letter is {self.chosen_letter}, now answer the questions!")
        self.game_running = True
        self.right_answers = 0
        self.question = None
        self.first_letter = None


variable = objects()


def game():
    object = random.choice(variable.subjects)
    variable.question = input(f"Enter a {object} that started with {variable.chosen_letter} : ")
    variable.subjects.remove(object)
    variable.first_letter = variable.question[0]


def logic():
    if variable.first_letter == variable.chosen_letter:
        variable.right_answers += 1
    if len(variable.subjects) == 0:
        print(f"You got {variable.right_answers} questions right!")
        variable.game_running = False


def main():
    game()
    logic()


while variable.game_running:
    main()

