# WAP to input user's first name & print it's length

name = input("Enter your name: ")
print(len(name.split(" ")[0]))

# WAP to find the occurances of '$' in a string

place = 'BBSR@Patia$$'
print(place.count('$'))

# WAP to check if a number entered by the user is odd or even

num = int(input("Enter a number: "))

if(num % 2 == 0 and num != 0):
    print(f"{num} is even.")
elif(num %2 != 0 and num != 0):
    print(f"{num} is odd.")
else:
    print("Zero")

# WAP to find the greatest of 3 numbers entered by user.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if((num1 > num2) and (num1 > num3)):
    print(f"{num1} is greater than {num2} and {num3}")
elif((num2 > num3) and (num2 > num1)):
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num2} and {num1}")


# WAP to check if a number is multiple of 7 or not

num7 = int(input("Enter a number: "))

if(num7 % 7 == 0):
    print(f"{num7} is a multiple of 7")
else:
    print(f"{num7} is not a multiple of 7")