import random

words = ["python", "computer", "keyboard", "function", "developer"]
hangman_drawings = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def play_round():

    word = random.choice(words)
    word_display = [ "_" for _ in word]
    wrong_guesses = 0
    guessed_letters = []

    while wrong_guesses < 6:
        print(hangman_drawings[wrong_guesses])
        print("Word:" + " ".join(word_display))
        print("Guessed: " + ", ".join(guessed_letters))
        if "_" not in word_display:
            print(f"You won! The word was: {word}")
            break   
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter exacly one letter.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    word_display[i]=guess               
        else:
            wrong_guesses += 1
            print(f"Nope. Wrong guesses: {wrong_guesses}/6")

    if wrong_guesses == 6:
        print(hangman_drawings[6])
        print(f"Game over! The word was: {word}")

while True:
    play_round()
    play_again = input("Do you want to play again ? (yes/no): ").lower()
    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break
