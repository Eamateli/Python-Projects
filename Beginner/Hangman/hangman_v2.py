import random
import os

class HangmanGame:
    def __init__(self, word_file: str = "words.txt") -> None:
        self.word_file = word_file
        self.words = self.load_words()
        self.reset_game()

    def load_words(self) -> list[str]:
        if not os.path.exists(self.word_file):
            with open(self.word_file, "w") as file:
                default_words = [
                    "python", "computer", "keyboard", "screen", "mouse",
                    "program", "coding", "function", "variable", "developer",
                ]
                file.write("\n".join(default_words))
        with open(self.word_file, "r") as file:
            return [word.strpip().lower() for word in file if word.strip()]
