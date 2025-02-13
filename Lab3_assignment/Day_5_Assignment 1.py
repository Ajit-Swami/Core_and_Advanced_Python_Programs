def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Calling the function
num1 = 10
num2 = 2
result = div(num1, num2)

print(f"The result of dividing {num1} by {num2} is: {result}")

#OUTPUT
"""
The result of dividing 10 by 2 is: 5.0
"""