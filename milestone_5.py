import random
from milestone_2 import word_list

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(self.word_guessed)


   
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        
    
    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ').lower()
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_lives > 0:
                game.ask_for_input()
                if game.num_letters == 0:
                   print(f"Congratulations, you correctly guessed {game.word}. You have won!")
                   break

play_game(word_list)