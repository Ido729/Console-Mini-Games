class objects:
    def __init__(self):
        self.answer = ["A", "B", "C"]
        self.questions = ["Which is the most common drink in Europe? ",
                          "What is Elon Musk car company? ",
                          "How many stars in the USA flag? "]

        self.answers = ["Beer", "Water", "Wine",
                        "Mazda", "Tesla", "Ferrari",
                        "50", "47", "52",]

        self.game_running = True
        self.questions_left = 3
        self.count_right = 0
        self.new_line = "-----------------------"


var = objects()


def First_question():
    A = 0
    B = 1
    C = 2
    answers_options = [f"A.{var.answers[A]}",
                       f"B.{var.answers[B]}",
                       f"C.{var.answers[C]}"]
    joined_string = "\n".join(answers_options)
    first = var.questions[0]
    print(first)
    print(joined_string)
    player_answer = input("Your answer: ")
    for answer in player_answer:
        answer = var.answer[0]
        if player_answer == answer:
            var.count_right += 1
            print("Right!")
        else:
            print("Wrong!")
    print(var.new_line)
    var.questions_left -= 1


def Secondary_question():
    A = 3
    B = 4
    C = 5
    answers_options = [f"A.{var.answers[A]}",
                       f"B.{var.answers[B]}",
                       f"C.{var.answers[C]}"]
    joined_string = "\n".join(answers_options)
    second = var.questions[1]
    print(second)
    print(joined_string)
    player_answer = input("Your answer is: ")
    for answer in player_answer:
        answer = var.answer[1]
        if player_answer == answer:
            var.count_right += 1
            print("Right!")
        else:
            print("Wrong!")
    print(var.new_line)
    var.questions_left -= 1


def Third_question():
    A = 6
    B = 7
    C = 8
    answers_options = [f"A.{var.answers[A]}",
                       f"B.{var.answers[B]}",
                       f"C.{var.answers[C]}"]
    joined_string = "\n".join(answers_options)
    third = var.questions[2]
    print(third)
    print(joined_string)
    player_answer = input("Your answer is: ")
    for answer in player_answer:
        answer = var.answer[0]
        if player_answer == answer:
            var.count_right += 1
            print("Right!")
        else:
            print("Wrong!")
    print(var.new_line)
    var.questions_left -= 1


def game_over():
    if var.questions_left == 0:
        print(f"Game over, You've right in {var.count_right} questions!")
        var.game_running = False


def game():
    First_question()
    Secondary_question()
    Third_question()
    game_over()


while var.game_running:
    game()
