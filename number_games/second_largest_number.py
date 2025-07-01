import random

length_list = int(input("Enter the length of the list: "))

def second_largest_number():
    numbers_list = []
    for i in range(1, length_list + 1):
        a = random.randint(1, 100)
        numbers_list.append(a)

    ori_list = numbers_list.copy()
    print(f"Generated list: {ori_list}")

    largest = max(numbers_list)
    numbers_list.remove(largest)
    second_largest = max(numbers_list)

    attempt = 0
    turns = 3
    guesses = 0

    while attempt < turns:
        guess = int(input("Enter the second largest number: "))
        guesses += 1
        attempt += 1

        if guess not in ori_list and attempt < turns:
            print(f"{guess} is not in the list. Try again.")
        elif guess == second_largest:
            print(f"Congrats! The second largest number is {second_largest}.")
            break
        elif attempt < turns:
            print("Try again.")
        else:
            print(f"Sorry! Game over. The second largest number is {second_largest}")

second_largest_number()