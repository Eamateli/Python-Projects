import random
import os

class HangmanGame:
    def __init__(self, word_file: str = "words.txt") -> None:
        self.word_file = word_file
        self.words = self.load_words()
        self.reset_game()