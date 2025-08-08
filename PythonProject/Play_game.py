from random import randrange

def play_game():
    numberRange = input("Input the number range you want to guess: ")
    numberRange = int(numberRange)
    num = randrange(1, numberRange + 1)
    try_sum = 1
    while True:
        guess = input("Guess the number: ")
        guess = int(guess)
        if guess > num:
            print("Larger")
            try_sum += 1
        elif guess < num:
            print("Smaller")
            try_sum += 1
        else:
            print(f"Nice work! You use {try_sum} times to reach the target number")
            return
