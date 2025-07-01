import random

num = int(input("Find the missing number between 1 - "))

missing = random.randint(1, num)

def missing_list():
    list_of_num = []
    for i in range(1, num + 1):
        list_of_num.append(i)

    list_of_num.remove(missing)
    random.shuffle(list_of_num)

    print(list_of_num)

    attempt = 0
    turns = 3
    print(f"You have {turns} turns to guess the number.")

    while attempt < turns:
        guess = int(input("Enter the missing number: "))

        if guess == missing:
            print("Congrats! you guessed the number")
            break
        else:
            attempt += 1
            if attempt < turns:
                print("Try again")
            else:
                print(f"Sorry! The missing number was {missing}")

missing_list()



