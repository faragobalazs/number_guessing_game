import random
from art import logo
print(logo)

NUMBER = random.randint(1,100)

def easy():
    '''This function if runs the easy mode of the game.'''
    attempts = 10

    def guessing(attempts):
        if attempts > 0:
            pass
        else:
            print("\nYou've run out of guesses. Game over. 😵")
            last_question()

        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < NUMBER:
            print("\nToo low. Guess again. ⬆️")
            attempts -= 1
            guessing(attempts)
        elif guess > NUMBER:
            print("\nToo high. Guess again. ⬇️")
            attempts -= 1
            guessing(attempts)
        else:
            print(f"\nYou got it! The answer was {NUMBER}. 👌")
            last_question()

    guessing(attempts)

def hard():
    '''This function if runs the hard mode of the game.'''
    attempts = 5

    def guessing(attempts):
        if attempts > 0:
            pass
        else:
            print("\nYou've run out of guesses. Game over. 😵")
            last_question()

        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < NUMBER:
            print("\nToo low. Guess again. ⬆️")
            attempts -= 1
            guessing(attempts)
        elif guess > NUMBER:
            print("\nToo high. Guess again. ⬇️")
            attempts -= 1
            guessing(attempts)
        else:
            print(f"\nYou got it! The answer was {NUMBER}. 👌")
            last_question()

    guessing(attempts)


def game():
    '''This function is the main function of the game.'''
    print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()
    else:
        game()


def last_question():
    '''This function asks the player to play again at the end of the game.'''
    game_again = input("Would you like to play again? 'yes' or 'no'? ").lower()

    if game_again == "yes":
        game()
    elif game_again == "no":
        print("Good bye! 👋")
        exit()
    else:
        last_question()

game()
