import random

guesses = 0
random_number = random.randint(1,100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    else:
        print("Congrats! It's Correct.")
        break

print(f"It took you {guesses} guesses")