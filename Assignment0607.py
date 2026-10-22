#Sebastian Tapia IS 303
#Description: Functions for the Wordle guessing game

import random


# Choose a random five-letter word
def choose_word():
    words = ["plant", "crane", "slate", "brick", "house",
             "chair", "grape", "stone", "flame", "bread"]

    secret_word = random.choice(words)
    return secret_word


# Get a valid guess from the player
def get_guess(previous_guesses):
    guess = input("Enter a five-letter word: ").lower()

    while len(guess) != 5 or not guess.isalpha() or guess in previous_guesses:
        if len(guess) != 5 or not guess.isalpha():
            print("Sorry, your guess must be exactly five letters.")
        else:
            print("You already guessed that word. Try again.")

        guess = input("Enter a five-letter word: ").lower()

    return guess


# Compare the guess to the secret word
def evaluate_guess(guess, secret_word):
    feedback = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback


# Display the guess and feedback
def display_guess(guess, feedback):
    print("Guess:", " ".join(guess.upper()))
    print("Feedback:", " ".join(feedback))


# Check if the player won
def has_won(guess, secret_word):
    if guess == secret_word:
        return True
    else:
        return False
