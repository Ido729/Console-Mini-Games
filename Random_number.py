import random


def main():
    secret_number = random.randint(0, 100)
    tries_left = 9
    print("You have 10 tries to guess the secret number.")

    while True:
        guess_number = int(input("Guess a number between 1 to 100: "))
        if guess_number < secret_number:
            print(f"to small bozo, only {tries_left} tries are left.")
            tries_left -= 1
        elif guess_number > secret_number:
            print(f"to big bozo, only {tries_left} tries are left.")
            tries_left -= 1
        print(" ")

        if guess_number == secret_number:
            print("good job, you guessed the secret number!")
            break
        elif tries_left == -1:
            print(f"you've lost all of your tries bozo, the secret number was {secret_number}")
            break


if __name__ == "__main__":
    main()
