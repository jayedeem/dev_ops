"""Import Libs"""
import random
import os

NUMBER = 20


class GuessTheNumber:
    """Guess The Number game"""

    def __init__(self, number_limit, tries) -> None:
        self.number_limit: int = number_limit
        self.guesses_taken: int = 0
        self.random_number: int = random.randint(1, self.number_limit)
        self.guess: int = None
        self.tries: int = tries

    def get_guess(self) -> bool:
        """Get the user input"""
        print('Guess a number between 1 and', self.number_limit)
        try:
            self.guess = int(input())
        except ValueError:
            print('Not a valid guess.')
            return False

        return True

    def play(self) -> None:
        """Game Controller"""

        while self.guesses_taken < self.difficulty():
            if not self.get_guess():
                continue

            self.guesses_taken += 1

            print(f'You have {self.guesses_taken} out of {self.difficulty()}')

            if self.guess == self.random_number:
                print(
                    f'You guessed the number in {self.guesses_taken} guesses!')
                break

            if self.guess < self.random_number:
                print('Your guess is too low.')

            if self.guess > self.random_number:
                print('Your guess is too high.')

            if self.tries >= 4:
                if self.guess - self.random_number == 2 or self.random_number - self.guess == 2:
                    print('Pretty close to guessing the correct number!')

        print(f'The correct number is {self.random_number}')

    def difficulty(self):
        """Set difficulty"""
        if self.tries == 1:
            self.tries = 1
            print("Whoa there! Lets see you try this in 1 shot!")
        if self.tries == 6:
            self.tries = 6
            print("Might be too easy!")

        return self.tries


def main() -> None:
    """Init the game"""
    while True:
        user_choice = input('Would you like to play a game? (y/q to quit) ')
        if user_choice.lower().startswith('q'):
            print("Thanks for playing!")
            break

        try:
            if user_choice not in ('y'):
                continue
        except ValueError:
            continue

        if user_choice == 'y':
            number_of_guesses = int(
                input('How many tries would you like to have? Between 1 and 6 '))
            try:
                if number_of_guesses < 1 or number_of_guesses > 6:
                    print('Pick a number between 1 and 6 only')
                    continue
            except ValueError:
                continue
            new_game = GuessTheNumber(NUMBER, number_of_guesses)
            new_game.play()
        print("\nPlay Again?")


if __name__ == "__main__":
    os.system("clear")
    main()
