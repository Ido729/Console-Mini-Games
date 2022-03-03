class objects:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D


        self.answers = ["A", "B", "C", "D"]

        self.questions = ["Which is the most common drink in Europe? ",
                          "What is Elon Musk car company? ",
                          "How many stars in the USA flag? ",
                          "What is a tomato? "]

        self.game_running = True
        self.questions_left = 4
        self.count_right = 0
        self.grade = 0
        self.answer = None
        self.new_line = "-----------------------"

    def details(self):
        print(f"A.{self.A}")
        print(f"B.{self.B}")
        print(f"C.{self.C}")
        print(f"D.{self.D}")


var = objects(1, 2, 3, 4)


def First_question():
    words = objects("Beer", "Water", "Wine", "tea")
    first = var.questions[0]
    print(first)
    words.details()
    var.answer = var.answers[0]
    checking()


def Secondary_question():
    words = objects("Mazda", "Tesla", "Toyota", "Ferrari")
    second = var.questions[1]
    print(second)
    words.details()
    var.answer = var.answers[1]
    checking()


def Third_question():
    words = objects(69, 47, 52, 50)
    third = var.questions[2]
    print(third)
    words.details()
    var.answer = var.answers[3]
    checking()


def fourth_question():
    words = objects("Vegetable", "Fruit", "Protein", "Herb")
    fourth = var.questions[3]
    print(fourth)
    words.details()
    var.answer = var.answers[1]
    checking()


def checking():
    player_answer = input("Your answer is: ")
    if player_answer == var.answer:
        var.grade += 25
        var.count_right += 1
        print("Right!")
    else:
        print("Wrong!")
    print(var.new_line)
    var.questions_left -= 1


def game_over():
    if var.questions_left == 0:
        print(f"You've guessed {var.count_right} questions right, Your grade is {var.grade}!")
        var.game_running = False



def game():
    First_question()
    Secondary_question()
    Third_question()
    fourth_question()
    game_over()


while var.game_running:
    game()

