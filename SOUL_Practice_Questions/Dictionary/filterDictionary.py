# Write a Python program to filter dictionaries from a list based on a condition.

list1 = [
    {
        "name": "Aditya",
        "roll": 28,
        "sic": "20BECA21"
    },
    {
        "name": "Ayush",
        "roll": 30,
        "sic": "20BCTB52"
    }
]

name = input("Enter the name you want to search: ")

for dict in list1:
    if(dict["name"] == name):
        print(dict)
    else:
        continue