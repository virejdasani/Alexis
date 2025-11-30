import requests
import random

class WoordleGame:
    def __init__(self):
        self.word = self.get_random_word()
        self.max_attempts = 6

    def get_random_word(self):
        """Fetches a random 5-letter word from the API."""
        try:
            response = requests.get("https://random-word-api.herokuapp.com/word?number=1&length=5")
            response.raise_for_status()
            word = response.json()[0]
            return word.lower()
        except Exception as e:
            print("Error fetching word from API. Falling back to a default word.")
            print(f"Error: {e}")
            fallback_words = ["apple", "grape", "stone", "chair", "table"]
            return random.choice(fallback_words)

    def get_feedback(self, guess):
        """Generates feedback for the user's guess."""
        feedback = []
        for i, letter in enumerate(guess):
            if letter == self.word[i]:
                feedback.append("🟩")  # Green square
            elif letter in self.word:
                feedback.append("🟨")  # Yellow square
            else:
                feedback.append("⬜")  # Gray square
        return feedback

    def play(self):
        """Runs the Wordle game."""
        print("Welcome to Wordle!")
        print("Guess the 5-letter word. You have 6 attempts.")
        
        attempts = 0
        while attempts < self.max_attempts:
            guess = input(f"Attempt {attempts + 1}/{self.max_attempts}: ").lower()

            # Validate the guess
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid input. Please enter a 5-letter word.")
                continue

            attempts += 1
            feedback = self.get_feedback(guess)
            print("Feedback: ", " ".join(feedback))

            if guess == self.word:
                print(f"🎉 Congratulations! You guessed the word: {self.word}")
                return

        print(f"Game over! The word was: {self.word}")

# Run the game
# if __name__ == "__main__":
#     wordle = WordleGame()
#     wordle.play()
