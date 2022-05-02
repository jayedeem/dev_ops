"""Random Mod"""
import random


def guess_random_number(tries: int, start: int, stop: int) -> None:
    """User Input Guess"""
    random_number = random.randint(start, stop)
    while tries != 0:
        print(f"Tries remaining {tries}")
        print(f"Guess a number from {start} and {stop}")
        user_input = int(input("Guess the number: "))

        if user_input == random_number:
            print('You guess the number!')
            break
        if user_input > random_number:
            tries -= 1
            print("Guess Lower!")
        if user_input < random_number:
            tries -= 1
            print("Guess Higher")


# guess_random_number(6, 0, 10)


def guess_random_linear(tries: int, start: int, stop: int) -> None:
    """Linear"""
    random_number = random.randint(start, stop)
    print(f"Guess a number from {start} and {stop}")
    found = False
    computer_tries = 0

    while tries > 0 and not found:
        for i in range(start, random_number):
            computer_guess = random.randint(start, stop)
            print(f"Tries remaining: {tries}")

            if computer_guess == i:
                print(
                    f"The computer guessed the correct number {random_number} in {computer_tries} tries ")
                found = True
                break

            print(f"The computer is guessing... {computer_guess}")
            computer_tries += 1
            tries -= 1

            if tries == 0:
                print('The program has failed to guess the correct')
                break
    return found


# guess_random_linear(10, 0, 10)


def guess_random_num_binary(tries: int, start: int, stop: int) -> None:
    """Binary Search"""
    random_number = random.randint(start, stop)
    found = False
    upper = stop
    lower = start
    print(f"Random number to find: {random_number}")

    while tries > 0 and not found:
        mid = (lower + upper) // 2

        if random_number == mid:
            print(f"Found it! {random_number}")
            found = True
        else:
            if random_number < mid:
                upper = mid - 1
                print("Guess Lower")

            else:
                lower = mid + 1
                print("Guess Higher")
            tries -= 1

        if tries == 0:
            print("Your program failed to find the number.")
            break

    return found


guess_random_num_binary(5, 0, 5)
