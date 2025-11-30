import random
import requests

class Hangman:
    def get_random_word(self):
        try:
            # Fetch a random word from the API
            response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            response.raise_for_status()
            word = response.json()[0]
            return word.lower()  # Ensure the word is in lowercase
        except Exception as e:
            print("Could not fetch a word from the API. Falling back to default word list.")
            print(f"Error: {e}")
            # Fallback word list
            fallback_words = ['python', 'developer', 'hangman', 'programming', 'challenge']
            return random.choice(fallback_words)

    def run_hangman(self):
        # Hangman states
        hangman_stages = [
            """
            -----
            |   |
                |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            /|   |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            /|\\  |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            /|\\  |
            /    |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            /|\\  |
            / \\  |
                |
            ---------
            """,
        ]
        
        # Use self.get_random_word() to fetch the word
        word_to_guess = self.get_random_word()
        guessed_word = ['_'] * len(word_to_guess)
        guessed_letters = set()
        attempts = len(hangman_stages) - 1  # Number of wrong guesses allowed

        print("Welcome to Hangman!")
        print("Guess the word one letter at a time.")
        print(f"The word has {len(word_to_guess)} letters.")

        while attempts > 0 and '_' in guessed_word:
            print(hangman_stages[len(hangman_stages) - 1 - attempts])
            print("\nWord to guess: ", ' '.join(guessed_word))
            print(f"Attempts remaining: {attempts}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
            
            guess = input("Enter a letter: ").lower()
            
            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print("You've already guessed that letter. Try a different one.")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word_to_guess:
                print(f"Good job! '{guess}' is in the word.")
                # Update guessed_word
                for index, letter in enumerate(word_to_guess):
                    if letter == guess:
                        guessed_word[index] = guess
            else:
                print(f"Oops! '{guess}' is not in the word.")
                attempts -= 1

        # End of the game
        print(hangman_stages[len(hangman_stages) - 1 - attempts])
        if '_' not in guessed_word:
            print("\nCongratulations! You guessed the word:", word_to_guess)
        else:
            print("\nGame over! The word was:", word_to_guess)