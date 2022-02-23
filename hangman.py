def main():
    secret_word = "burger"
    guesses = []
    already_guessed = []
    guess_left = 11
    finish = False

    while not finish:
        guessing = input("guess a letter: ")
        guesses.append(guessing)
        for letters in secret_word:
            if letters in guesses:
                print(letters, end=" ")
            else:
                print("_", end=" ")
            if letters in already_guessed:
                already_guessed.append(guessing)
        print(" ")

        if guessing not in secret_word:
            guess_left -= 1
            print(f"you've guessed wrong, only {guess_left} guesses are left")
            already_guessed.append(guessing)
            if guess_left == 0:
                break
        print(f"(these letters have already been guessed: {', '.join(already_guessed)})")
        print(" ")

        finish = True
        for letters in secret_word:
            if letters not in guesses:
                finish = False
    if finish:
        print("You successfully guessed the word!")
    else:
        print(f"You lost, the secret word was {secret_word}")


if __name__ == "__main__":
    main()
