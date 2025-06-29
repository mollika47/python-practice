# Using custom function

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result
print(factorial(5))


# Using built-in function

n = int(input("Enter a number: "))
res = factorial(n)
print(f"Factorial of {n}! is ", + res)