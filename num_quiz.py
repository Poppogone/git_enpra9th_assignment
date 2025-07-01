import random

def give_hint(secret,guess):
    return

def num_guess_game():
    ans = str(random.randint(100,999))
    max_attempts = 0
    attempts = 0

    num_difficulty = int(input("Difficulty  Easy:0 Normal:1 Hard:2 (input the number)"))
    if num_difficulty == 0:
        max_attempts = 15
    elif num_difficulty == 1:
        max_attempts = 10
    elif num_difficulty == 2:
        max_attempts = 5
    
    print("Guess the 3-digits number!")

    while attempts < max_attempts:
        guess = input(f"input ur answer(attempts:{attempts + 1}) : ")
        
        attempts += 1

        if guess == ans:
            print(f"Correct! You guessed it in {attempts} tries.")
            break
        else:
            hint = give_hint(ans,guess)
            #hint
    else:
        print(f"Out of attempts! The correct number was {ans}.")
    
if __name__ == "__main__":
    num_guess_game()

