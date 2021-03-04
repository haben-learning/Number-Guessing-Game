"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("_" * 38)
    # Introduces user with a Welcome banner
    print("", "Welcome to the Number Guessing Game!")
    print("_" * 38)
    # Creates a random number
    answer = random.randint(1, 10)
    attempts = 1
    scores_list = []
    # Prompts user for a guess
    while True:
        try:
            guess = int(input("Pick a number between numbers 1 and 10: "))
            if guess > 10 or guess < 1:
                raise Exception("Oh no! You choose a number that isn't within the range of 1 and 10")
        except ValueError:
            print("Sorry that is not a number! Please try again")
        except Exception as e:
            print(e)
        else:
            # Checks users guess whether it is higher or lower than the answer
            if guess > answer:
                print("It's lower")
                attempts += 1
            elif guess < answer:
                print("It's higher")
                attempts += 1
            # When users guess matches the answer a message is displayed with the
            # Appropriate message and stats
            elif guess == answer:
                if attempts == 1:
                    print("You guessed the right answer on your first try! WELL DONE!")
                    while True:
                        try:
                            play_again = input("Would you like to play again? Y/N: ").upper()
                            if play_again == "Y":
                                scores_list.append(attempts)
                                print("The HIGHSCORE is {}".format(min(scores_list)))
                                answer = random.randint(1, 10)
                                attempts = 1
                                break
                            if play_again == "N":
                                print("Closing game, thanks for playing!")
                                break
                            if play_again != "Y":
                                raise ValueError("Please select either 'Y' or 'N' to proceed")
                            if play_again != "N":
                                raise Exception("Please select either 'Y' or 'N' to proceed")
                        except ValueError as e:
                            print(e)
                            continue
                        except Exception as e:
                            print(e)
                            continue
                else:
                    print("You got it! It took you {} tries.".format(attempts))
                    while True:
                        try:
                            play_again = input("Would you like to play again? Y/N: ").upper()
                            if play_again == "Y":
                                scores_list.append(attempts)
                                print("The HIGHSCORE is {}".format(min(scores_list)))
                                answer = random.randint(1, 10)
                                attempts = 1
                                break
                            if play_again == "N":
                                print("Closing game, thanks for playing!")
                                break
                            if play_again != "Y":
                                raise ValueError("Please select either 'Y' or 'N' to proceed")
                            if play_again != "N":
                                raise Exception("Please select either 'Y' or 'N' to proceed")
                        except ValueError as e:
                            print(e)
                            continue
                        except Exception as e:
                            print(e)
                            continue
# Kick off the program by calling the start_game function.
start_game()