num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if(num1 >= num2 and num2 >= num3):
    print(f"{num1} is largest among {num2} and {num3}")
elif(num2 >= num1 and num2 >= num3):
    print(f"{num2} is largest among {num1} and {num3}")
else:
    print(f"{num3} is largest among {num1} and {num2}")