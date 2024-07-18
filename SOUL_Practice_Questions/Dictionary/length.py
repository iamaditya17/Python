# Write a program to find the length of a dictionary.

dict1 = {}

length = int(input("Enter the length of dictionary: "))

for i in range(length):
    key = input()
    value = input()

    dict1[key] = value

print("Length of dictionary is: ",len(dict1))

# Write a program to iterate over a dictionary and print each key and value.

for key in (dict1.items()):
    print(key)