def main():
    chosen = {
        "ok": "in this game, you need to chose between 2 options, one mistake and you lost.",
        "right": "you've walked into a room with huge octopus!",
        "sword": "You killed the octopus, GG",
        "gun": "The gun doesnt affect the monster, she killed you, start over.",
        "left": "You've walked into a room with a giant dragon!",
        "crossbow": "Your actually thought its gonna kill it, you have lost start over",
        "RPG": "great job soldier, the dragon is dead."
    }

    first_question = input('Type "ok" if tou want to play: ')
    if first_question == "ok":
        print(chosen.get("ok"))
        second_question = input("chose between right and the left room: ")

        if second_question == "right":
            print(chosen.get("right"))
            third_question = input("you have to kill that shit, do you wanna use sword or a gun? ")
            if third_question == "sword":
                print(chosen.get("sword"))
            elif third_question == "gun":
                print(chosen.get("gun"))

        elif second_question == "left":
            print(chosen.get("left"))
            four_question = input("you have to kill that shit, do you wanna use crossbow or an RPG? ")
            if four_question == "crossbow":
                print(chosen.get("crossbow"))
            elif four_question == "RPG":
                print(chosen.get("RPG"))


main()
