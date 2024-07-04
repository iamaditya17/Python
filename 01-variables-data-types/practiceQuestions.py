# Write a program to input 2 numbers and print their sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2

print(f"Sum of {num1} and {num2} is: ", total) # here f is used as a f-string (formatted string literal) to embed the variables directly within the string

# WAP to input side of a square & print its area

side = float(input("Enter the side of square: "))

print("Area of the square is: ", side ** 2)

# WAP to input 2 floating point numbers and print their average

val1 = float(input("Enter the first value: "))
val2 = float(input("Enter the second value: "))

avrg = (val1 + val2) / 2

print("The average of two numbers is: ", avrg)

# WAP to input 2 int numbers a &b, Print true if a is greater than or equal to b. If not print false

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a >= b:
    print(True)
else:
    print(False)
