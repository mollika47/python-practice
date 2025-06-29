# Using built-in function

Numbers = [11, 2, 32, 5,  7, 69]
total = sum(Numbers)
print(f"{Numbers} = {total}")


# Using custom function

def total(*numbers):
    result = 0
    for i in numbers:
        result += i
    return f"Total is {result}"
print(total(5, 6, 1, 54))