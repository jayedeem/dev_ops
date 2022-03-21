import random


HIGH_SCORE = 0


def dice_game():
    total = 0
    while True:
        global HIGH_SCORE
        print(f"Current High Score: {HIGH_SCORE}")
        user_choice = int(input(
            "1) Roll Dice\n2) Leave Game\nEnter your choice: "))
        if user_choice == 2:
            print("Goodbye!")
            break
        if user_choice == 1:
            current_roll = random.randint(0, 6)
            total += current_roll
            print(f"\nYou roll a.. {current_roll}")

            current_roll = random.randint(0, 6)
            print(f"You roll a.. {current_roll}")
            total += current_roll

            print("You have rolled a total of:", total, "\n")

        if total > HIGH_SCORE:
            HIGH_SCORE = total
            print("New High Score!\n")


dice_game()
