import random

def choose_word():
    word_list = ["python", "hangman", "programming", "computer", "algorithm", "code"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    
    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent Word:", current_display)
        
        if current_display == word_to_guess:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
            
            if attempts == max_attempts:
                print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)
                break

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()

