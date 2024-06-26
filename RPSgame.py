import random
from pywebio.input import *
from pywebio.output import *

# conditions ✂️📄🪨

lst = ["ROCK", "PAPER", "SCISSOR",]


def user_and_computer_choice():
    user_choice = select("Select Your Choice", lst)
    computer_choice = random.choice(lst)

    if user_choice == computer_choice:
        put_text("DRAW")
        put_text(f"Computer Choice -> {computer_choice}")
        put_text(f"Your Choice -> {user_choice}")

    elif user_choice == "ROCK" and computer_choice == "PAPER":
        put_text("YOU LOSE")
        put_text(f"Computer Choice -> {computer_choice}")
        put_text(f"Your Choice -> {user_choice}")

    elif user_choice == "PAPER" and computer_choice == "SCISSOR":
        put_text("YOU LOSE")
        put_text(f"Computer Choice -> {computer_choice}")
        put_text(f"Your Choice -> {user_choice}")

    elif user_choice == "SCISSOR" and computer_choice == "ROCK":
        put_text("YOU  LOSE")
        put_text(f"Computer Choice -> {computer_choice}")
        put_text(f"Your Choice -> {user_choice}")

    else:
        put_text("YOU WIN")
        put_text(f"Computer Choice -> {computer_choice}")
        put_text(f"Your Choice -> {user_choice}")


def main():
    put_text("Game")
    choice = ["Play", "Exit"]
    while True:
        user = select("Want play or exit", choice)
        if user == "Play":
            user_and_computer_choice()
        elif user == "Exit":
            put_text("Exited")
            break
        else:
            put_text("Invalid Choice")
            break


if __name__ == "__main__":
    main()
