import random

VALID_OPTIONS = ["R", "P", "S"]


def display_full_form(choice_letter):
    FULL_FORMS = ["Rock", "Paper", "Scissors"]
    return FULL_FORMS[VALID_OPTIONS.index(choice_letter)]


def decide_winner(human_choice, robot_choice):
    if human_choice == "R":
        if robot_choice == "S":
            print(f"\n{display_full_form(human_choice)} crushes {display_full_form(robot_choice)}")
            return "You won!"
        elif robot_choice == "P":
            print(f"\n{display_full_form(robot_choice)} covers {display_full_form(human_choice)}")
            return "Computer won!"
        else:
            return "It's a tie!"

    if human_choice == "P":
        if robot_choice == "R":
            print(f"\n{display_full_form(human_choice)} covers {display_full_form(robot_choice)}")
            return "You won!"
        elif robot_choice == "S":
            print(f"\n{display_full_form(robot_choice)} cuts {display_full_form(human_choice)}")
            return "Computer won!"
        else:
            return "It's a tie!"

    if human_choice == "S":
        if robot_choice == "P":
            print(f"\n{display_full_form(human_choice)} cuts {display_full_form(robot_choice)}")
            return "You won!"
        elif robot_choice == "R":
            print(f"\n{display_full_form(robot_choice)} crushes {display_full_form(human_choice)}")
            return "Computer won!"
        else:
            return "It's a tie!"


def main():
    user_choice =  input("Enter R, P or S: ").upper()
    while user_choice not in VALID_OPTIONS:
        print("Invalid entry!")
        user_choice =  input("\nEnter R, P or S: ").upper()

    computer_choice = random.choice(VALID_OPTIONS)
    print(f"\nPlayer ({display_full_form(user_choice)}) : CPU ({display_full_form(computer_choice)})")

    decision = decide_winner(user_choice, computer_choice)
    print(decision)

    if decision == "It's a tie!":
        main()
    else:
        print("Game over!\n")


print("\n--| ROCK PAPER SCISSORS |--")
main()
