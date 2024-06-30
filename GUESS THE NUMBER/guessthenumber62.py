import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(levels):
    if levels=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif levels=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    elif guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    else:
        print(f"your Guess is right...the answer was {answer}")
    
def game():
    print(logo_art.logo)
    print("let me think of a number from 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("Choose level of difficulty 'easy' or 'hard':").lower()

    attempts=set_difficulty(level)
    if level!='easy' and level!='hard':
        print("you have entered wrong difficulty level...play again")
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} left to guess the number")
        guessed_number=int(input('guess a number:'))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("you are out of guesses...you lose!")
            return
        elif guessed_number!=answer:
            print("Guess again")
game()


