import random


def main():
    left_guesses = 10
    secret_words = ["fortnite", "battle", "royal"]
    print("You have 10 tries to guess the secret word, go!")

    while left_guesses != 0:
        sec_word = random.choice(secret_words)
        guessing = input("guess the word: ")

        if bool(guessing == sec_word):
            index = secret_words.index(sec_word)
            secret_words.pop(index)
            print(f"You've guessed RIGHT a word, {len(secret_words)} words left to guess")
        else:
            left_guesses -= 1
            print(f"You've guessed WRONG, {left_guesses} guesses are left")
        if left_guesses == 0 or len(secret_words) == 0:
            print("Theres no left guesses, game over.")
            break


if __name__ == "__main__":
    main()
