import random
import os

class GuessTheNumber:
    def __init__(self, number_limit, tries) -> None:
        self.number_limit: int = number_limit
        self.guesses_taken: int = 0
        self.number: int = random.randint(1, self.number_limit)
        self.guess: int = None
        self.tries: int = tries

    def get_guess(self) -> bool:
        print('Guess a number between 1 and', self.number_limit)
        try:
            self.guess = int(input())
        except ValueError:
            print('Not a valid guess.')
            return False

        return True

    def play(self) -> None:
        self.difficulty()
        while self.guesses_taken <  self.tries:
            if not self.get_guess():
                continue

            self.guesses_taken += 1

            if self.guess == self.number:
                print(f'You guessed the number in {self.guesses_taken} guesses!')
                break

            if self.guess < self.number:
                print('Your guess is too low.')

            if self.guess > self.number:
                print('Your guess is too high.')

            if self.guess - self.number == 1 or self.number - self.guess == 1:
                print('Pretty close to guessing the correct number!')

        print(f'The correct number is {self.number}')

    def difficulty(self):
        if self.tries == 1:
            self.tries = 1
            print("Whoa there lets see you try this in 1 shot")
        if self.tries == 6:
            self.tries = 6
            print("Might be too easy!")
        
        return self.tries

def main() -> None:
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
            number_of_guesses = int(input('How many tries would you like to have? Between 1 and 6 '))
            try:
                if number_of_guesses < 1 or number_of_guesses > 6:
                    print('Pick a number between 1 and 6 only')
                    continue
            except ValueError:
                continue
            new_game = GuessTheNumber(20, number_of_guesses)
            new_game.play()
        print("\nPlay Again?")

os.system("clear")
main()

