import random

words = ["python", "computer", "keyboard", "function", "developer"]

word = random.choice(words)

word_display = [ "_" for _ in word]

wrong_guesses = 0

while wrong_guesses < 6:
    print("Word:" + " ".join(word_display))
    if "_" not in word_display:
        print(f"You won! The word was: {word}")
        break
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                word_display[i]=guess
                
    else:
        wrong_guesses += 1
        print(f"Nope. Wrong guesses: {wrong_guesses}/6")

if wrong_guesses == 6:
    print(f"Game over! The word was: {word}")