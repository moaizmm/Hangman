import random


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
        """
        This function checks if the guessed letter is in the word.

        Parameters
        ----------
        guess : str
            The letter guessed by the player.

        Attributes
        ---------- 
        num_lives       : int
            Number of lives a player has. The number of lives reduces each time the user guesses an incorrect letter.
        word            : str
            Random word generated from the word_list.
        word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        num_letters     : int
        Length of unique letters in the 'word'.
        The number is decreased each time the letter is guessed correctly.
        list_of_guesses : list
        List of unique letters that have been guessed by the player. Appends a letter everytime a new letter is guessed.
        
        
        """
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
        
        
    
    def ask_letter(self):
        """
        Asks user to guess the letter and checks if the entered character is a single alphabetical
        character. and if the letter has already been guessed.
        """
    
        
        while True:
            guess = input('Enter a single letter: ').lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
        """
        This function to play the game based on number of lives and does the following checks:
        - If the number of lives is equal to 0 then player loses the game and game is ended.
        - If the number of lives are greater than 0 then the game continues.
        - If all the letter are guessed then the player has correctly guessed and has won.

        Parameters
        ----------
        word_list : list
            The word_list is list of fruits where one of the word chosen randomly which will need to be guessed by the player.
        
        """
    
        num_lives = 5
        game = Hangman(word_list, num_lives)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_lives > 0:
                game.ask_letter()
                if game.num_letters == 0:
                   print(f"Congratulations, you correctly guessed {game.word}. You have won!")
                   break
word_list = ['pomegranate', 'strawberries', 'pineapple', 'apple', 'grapes','lychee','cherry']
if __name__ == "__main__":
 play_game(word_list)