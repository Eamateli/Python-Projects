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


def main_v1():
    print("Welcome to Hangman!")
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's paly Hangman!")
    time.sleep(1)
    print("I'm thingking of a word...")
    time.sleep(1)


    word = random.choice(words)

    word_display = []
    for letter in word:
        word_display.append("_")

    wrong_guesses = 0
    guessed_letters= []

    while wrong_guesses < 6:
        print(hangman_drawings[wrong_guesses])
        print("Current word: " + " ".join(word_display))
        print("Letters guessed: " + ", ".join(guessed_letters))

        if "_" not in word_display:
            print(f"Congratulations! You guessed the word: {word}")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue


        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                        word_display[i] = guess
        else:
            print("Wrong guess!")
            wrong_guesses += 1

    if wrong_guesses == 6:
        print(hangman_drawings[wrong_guesses])
        print(f"Game Over! The word was: {word}")


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        main_v1()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main_v1()