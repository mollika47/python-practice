# Using the Exponentiation Operator **
x = 5
cube = x**3
print(cube)


# Using Built-in Function
a = 3
result = pow(a, 3)
print(result)


# Using a Custom Function and user input
def cube(num):
    return f"The cube of {num} is {num**3}"
print(cube(int(input("Enter a number: "))))
