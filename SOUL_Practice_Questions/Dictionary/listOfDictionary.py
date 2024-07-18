# Write a Python program to create a list of dictionaries.

list1 = []

dictNumber = int(input("Enter the no of dictionary you want to append in list: "))

for i in range(dictNumber):

    dict1 = {}

    length = int(input(f"Enter the length of dictionary {i+1}: "))

    for j in range(length):
        key = input()
        value = input()

        dict1[key] = value

    list1.append(dict1)

print(list1)