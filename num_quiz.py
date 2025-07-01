import random

def give_hint(secret,guess):
    E = 0 #Exact match(digit and position)
    B = 0 #Correct digit, but wrong postion

    secret_check = [False]*3
    guess_check = [False]*3 #To avoid double counting

    for i in range(3):
        if guess[i] == secret[i]:
            E += 1
            secret_check[i] = True
            guess_check[i] = True
    
    for i in range(3):
        if guess_check[i] == False:
            for j in range(3):
                if secret_check[j] == False and guess[i] == secret[j]:
                    B += 1
                    secret_check[j] = True
                    break

    return f"{E}E{B}B"

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
    

    print("Rule1: Number is 3-digits")
    print("Rule2: Ur digit and position is correct : E")
    print("Rule3: Only digit is correct(wrong position):B")
    print("ex) answer is 398")
    print("If u put 597 -> 1E0B")
    print("If u put 872 -> 0E1B")
    print("If u put 893 -> 1E2B")

    print("Guess the 3-digits number!")

    while attempts < max_attempts:
        guess = input(f"input ur answer(attempts:{attempts + 1}) : ")
        
        attempts += 1

        if guess == ans:
            print(f"Correct! You guessed it in {attempts} tries.")
            break
        else:
            hint = give_hint(ans,guess)
            print(f"Incorrect! Hint:{hint}")
            #hint
    else:
        print(f"Out of attempts! The correct number was {ans}.")
    
if __name__ == "__main__":
    num_guess_game()

