import random 
import time

#1.Create a list of words for the game

words = [
    "python", "computer", "keyboard", "screen", "mouse", "program",
    "coding", "function", "variable", "developer", "software"
]

#2.List of strings with the hangman drawing

hangman_drawings = [
    #0 wrong guesses
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    # 1 wrong guess
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # 2 wrong guesses
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 3 wrong guesses
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 4 wrong guesses
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # 5 wrong guesses
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # 6 wrong guesses (game over)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]