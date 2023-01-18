def nr_attempts():
    difficulty = input("please choose a difficulty level! hard or easy? ").lower()
    if difficulty == "hard":
        max_attempt = 5
        print(f"You have {max_attempt} to complete the game")
    else:
        max_attempt = 10
        print(f"you have {max_attempt} to complete the game")
    return max_attempt
#%%
# print(nr_attempts())
#%%
def check_answer(guess, answer, max_attempt):
    """check answer against guess, returns the remaining attempts"""
    if guess > answer:
        print("too high")
        return max_attempt - 1
    elif guess == answer:
        print("you won")
    else:
        print("too low")
        return max_attempt - 1
#%%
#%%
#%%
#%%
# print(nr_attempts())
#%%
#%%
#%%

from attempts import nr_attempts
# from guess import yr_guess
# from check_answer import check_answer
#%%
#%%
def game():
    print("welcome to the guess number!")
    # nr_attempts()
    max_attempts = nr_attempts()
    print("I am thinking of a number between 1 and 100!")
    import random
    answer = random.randint(1, 100)
    print(answer)
    guess = 0
    print(guess)
    
    while guess != answer:
        print(f"you have {max_attempts} attempts left.")
        guess = int(input("guess a number: "))
        max_attempts = check_answer(guess, answer, max_attempts)
        if max_attempts == 0:
            print("game over! You run out of guess. You lose!")
            break
        elif guess != answer:
            print("Guess again!")
        
        
    
#%%
game()

#%%


#%%


#%%
#%%
