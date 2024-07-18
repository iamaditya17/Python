# Write a Python program to add a new dictionary to a list of dictionaries.

studentDict = {
    "name": "Aditya",
    "roll": 28,
    "sic": "20BECA21"
}

companyDetails = {
    "company": "SOUL",
    "department": "IT"
}
 
newDict = {}

list1 = []

list1.append(studentDict)
list1.append(companyDetails)

length = int(input("Enter the length of new dictionary: "))

for i in range(length):
    key = input()
    value = input()

    newDict[key] = value

list1.append(newDict)

print(f"After adding the new dictionary, updated list is: {list1}")



