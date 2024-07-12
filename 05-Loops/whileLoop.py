i = 1

while (i <= 5):
    print(i)
    i += 1

print("Reverse")

i = 5

while(i >= 1):
    print(i)
    i -= 1

# Print numbers from 1 to 100

i = 1

while (i <= 100):
    print("Value is: ",i)
    i += 1

# Print numbers from 100 to 1

print("Displaying in reverse order")

i = 100

while(i >= 1):
    print("Value is: ",i)
    i -= 1

# Print the multipication table of a number n

i = 1
num = int(input("Please enter a number: "))

while(i <= 10):
    print(f"{num} * {i}: ",num * i)
    i += 1

# Print the elements of the following list using a loop

list1 = [1,4,9,16,25,36,49,64,81,100]
i = 0

while(i < len(list1)):
    print(list1[i])
    i += 1

# Search for a number x in this tuple

tup1 = (1,4,9,16,25,36,49,64,81,100,36)
i = 0

x = int(input("Enter a number: "))

while (i < len(tup1)):
    if(tup1[i] == x):
        print(f"{x} is found at index{i}")

    i += 1

# Print the even numbers and skip the odds

i = 1

while(i <= 10):
    if(i % 2 == 0):
        print(f"{i} is even")
        i += 1
    else:
        i += 1
        continue
    