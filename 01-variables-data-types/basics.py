name = "Aditya Patra"
age = 22
gender = 'Male'

print("Name: ",name , " ", "Age: ",age, " ","Gender: ",gender)

# If we want to know the data type of the above variables
print(type(name))
print(type(age))
print(type(gender))
print(type(0.60))

# If we want to print 2 different things in a single line
print("Hello","Aditya")

# Type Conversion
a = 2
b = 6.4

print(a + b) #2.0 + 6.4 => 8.4 (whenever we will perform some arithmetic operation between Int and Float the output will be Float)

# Type Casting
a = int("2")    #convert "2" into 2
b = 4.0

print(a + b)

# User Input using input()

name = str(input("Enter Your Name:"))

print("Your name is: ", name)