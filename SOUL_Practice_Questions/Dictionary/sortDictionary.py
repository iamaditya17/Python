# Write a program to sort the dictionary based on key.

dict1 = {
    "name": "Aditya",
    "roll": 28,
    "sic": "20BECA21",
    "club": ["Cricket","Football"]
}

for i in sorted(dict1):
    print(f"Key: {i} , value: {dict1[i]} ")