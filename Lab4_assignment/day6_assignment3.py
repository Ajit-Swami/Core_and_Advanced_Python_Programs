# Program to find the factorial of a given number using a while loop

num = int(input("Enter a number: "))  # Input the number
factorial = 1

# Using a while loop to calculate factorial
while num > 0:
    factorial *= num  # Multiply the current number
    num -= 1  # Decrease the number by 1

print("Factorial:", factorial)


'''
Output :-
Enter a number: 5
Factorial: 120

'''
