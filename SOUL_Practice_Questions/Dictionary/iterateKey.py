# Write a program to iterate over a dictionary and print each key and value.

dict1 = {
    "name": "Aditya",
    "roll": 28,
    "sic": "20BECA21",
    "club": ["Cricket","Football"]
}

for i in (dict1.items()):
    print(f"Key: {i[0]} , value: {i[1]}")