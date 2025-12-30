# Generate a random word and filler for that
random_word = "ant"
word_length = len(random_word)
filler_word = "_" * word_length # ___
attempts = 4
guessed_words = []

# take user guess

while attempts > 0 and filler_word != random_word:
    guess = input("Guess a Letter..").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in random_word:
        if guess in guessed_words:
            print("You have already guessed it.. try something else!!")
        else:
            guessed_words.append(guess)
            new_filler = ""
            for i in range(word_length):
                if random_word[i] == guess:
                    new_filler += guess
                else:
                    new_filler += filler_word[i]

            filler_word = new_filler
            print("Good guess")
    else:
        attempts -= 1
        print("Wrong guess")

    print("word: ", filler_word)
    print("Attempts: ", attempts)

if filler_word == random_word:
    print("Congratulations! You guessed the word.")
else:
    print("Game Over! The word was:", random_word)
 