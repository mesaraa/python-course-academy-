from random import choice
from data import words,hangman_art
import os

HINT_LIMITS = {
    "easy": 2,
    "medium": 1,
    "hard": 0
}

def select_difficulty():
    print("Choose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        difficulty = "easy"
    elif choice == "3":
        difficulty = "hard"
    else:
        difficulty = "medium"

    return difficulty

def init_game():
    random_word = choice(words)
    word_length = len(random_word)
    filler_word = "_" * word_length # ___
    difficulty = select_difficulty()

    attempts = len(hangman_art[difficulty]) - 1
    hints_left = HINT_LIMITS[difficulty]
    guessed_words = []
    return random_word, filler_word, attempts, guessed_words, word_length,difficulty, hints_left

def use_hints(word, filler, guessed_words, attempts):
    unrevealed_letters = []

    for i in range(len(word)):
        if filler[i] == "_":
            unrevealed_letters.append(word[i])

    if not unrevealed_letters:
        print("No letters left to reveal.")
        return filler, attempts
    
    hint_letter = choice(unrevealed_letters)
    guessed_words.append(hint_letter)

    new_filler = ""
    for i in range(len(word)):
        if word[i] == hint_letter:
            new_filler += hint_letter
        else:
            new_filler += filler[i]

    attempts -= 1
    print(f"Hint used! Revealed letter: {hint_letter}")

    return new_filler, attempts    

def process_guess(word, filler, guess, guessed_words, attempts,difficulty):
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        return filler, attempts

    if guess in guessed_words:
        print("You already guessed that letter.")
        return filler, attempts
    
    guessed_words.append(guess)

    if guess in word:
        new_filler = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_filler += guess
            else:
                new_filler += filler[i]
        print("Good guess!")
        return new_filler, attempts
    else:
        attempts -= 1
        print("Wrong guess!")
        stage_index = len(hangman_art[difficulty]) - 1 - attempts
        print(hangman_art[difficulty][stage_index])
        return filler, attempts
    
def play_game():
    random_word, filler_word, attempts, guessed_words, word_length, difficulty, hints_left= init_game()
    while attempts > 0 and filler_word != random_word:
        print("Word:", filler_word)
        print("Attempts:", attempts)
        print("Hints Left:", hints_left)

        guess = input("Guess a letter or (type hint for hint) ").lower().strip()
        os.system("cls" if os.name == "nt" else "clear")

        if guess == "hint":
            if hints_left > 0:
                filler_word, attempts = use_hints(
                    random_word,
                    filler_word,
                    guessed_words,
                    attempts
                )
                hints_left -= 1
            else:
                print("No Hints Available for this difficulty.")
            continue

        filler_word, attempts = process_guess(
            random_word,
            filler_word,
            guess,
            guessed_words,
            attempts,
            difficulty
        )

    if filler_word == random_word:
        print("Congratulations! You guessed the word.")
    else:
        print("Game Over! The word was:", random_word)

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break