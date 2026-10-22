
# Author: Sebastian Tapia
# Description: A Wordle game where the player has six attempts

from Assignment0607 import choose_word, get_guess, evaluate_guess, display_guess, has_won


# Welcome player
print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")


# Allow player to play again
play_again = "yes"

while play_again.lower() == "yes":

    # Start a new game
    secret_word = choose_word()
    previous_guesses = []
    attempts = 0
    won = False

    # Player gets six valid guesses
    while attempts < 6 and won == False:
        print()
        print("Attempt", attempts + 1, "of 6")

        # Get the player's guess
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)
        attempts += 1

        # Evaluate and display the guess
        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        # Check if the player guessed correctly
        won = has_won(guess, secret_word)

        if won:
            print("Congratulations! You solved the puzzle!")

    # If player used all six guesses
    if won == False:
        print("Sorry, you ran out of attempts!")
        print("The secret word was:", secret_word.upper())

    # Ask if the player wants to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()

print("Thanks for playing!")
