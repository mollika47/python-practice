# Using the Exponentiation Operator **
x = 5
square = x**2
print(square)


# Using Built-in Function
a = 3
result = pow(a, 2)
print(result)


# Using a Custom Function and user input
def square(num):
    return f"The square of {num} is {num**2}"
print(square(int(input("Enter a number: "))))