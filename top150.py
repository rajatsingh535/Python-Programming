# Problem 1: Sum of List Elements
# Ask user to input numbers separated by commas, then calculate the sum and average.
# Input: "10, 20, 30, 40, 50"
# Output: Sum = 150, Average = 30
n = input("Enter numbers separated by commas: ")
numbers = list(map(int, n.split(',')))
sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)
print(f"Sum: {sum_of_numbers}, Average: {average}")

# Problem 2: Factorial Calculation
# Given an integer input, calculate the factorial of the number.
# Input: 5
# Output: 120
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")

# Problem 3: Check Prime Number
# Check if a number is prime.
# Input: 7
# Output: 7 is a prime number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Problem 4: Fibonacci Sequence
# Print the Fibonacci sequence up to n terms.
# Input: 5
# Output: 0 1 1 2 3
num = int(input("Enter number of terms: "))
n1, n2 = 0, 1
print(n1, n2, end=" ")
for i in range(2, num):
    sum = n1 + n2
    print(sum, end=" ")
    n1, n2 = n2, sum

# Problem 5: Leap Year Checker
# Check if a given year is a leap year.
# Input: 2024
# Output: 2024 is a leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Problem 6: Pythagorean Theorem (Right Triangle Checker)
# Given the two sides of a right triangle, check if the hypotenuse is valid.
# Input: 3, 4
# Output: Hypotenuse = 5
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
import math
hypotenuse = math.sqrt(side1**2 + side2**2)
print(f"The hypotenuse is {hypotenuse}")

# Problem 7: Swap List Elements
# Swap the first and last element of a list.
# Input: [1, 2, 3, 4, 5]
# Output: [5, 2, 3, 4, 1]
my_list = [1, 2, 3, 4, 5]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("Swapped list:", my_list)

# Problem 8: Simple Calculator
# Perform basic arithmetic operations (+, -, *, /) on two numbers.
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/' and num2 != 0:
        result = num1 / num2
    else:
        result = "Invalid operation or division by zero."
    print("Result:", result)

calculator()

# Problem 9: Print Characters at Even Indices
# Input a string, and print characters at even indices.
# Input: "hello"
# Output: h l o
input_string = input("Enter a string: ")
for index in range(len(input_string)):
    if index % 2 == 0:
        print(input_string[index], end=' ')

# Problem 10: Leap Year Validator
# Determine if a year is a leap year or not.
# Input: 2000
# Output: 2000 is a leap year.
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
