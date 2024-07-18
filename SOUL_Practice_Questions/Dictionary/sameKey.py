# Write a Python program to check if all dictionaries in a list have a specific key.

list1 = [
    {
        "name": "Aditya",
        "roll": 28,
        "sic": "20BECA21",
        "subject": ["Math","DSA","DBMS","OOPS IN JAVA","SOFTWARE ENGINEERING"]
    },
    {
        "name": "Ayush",
        "roll": 30,
        "sic": "20BCTB52",
        "subject": ["Math","DSA","DBMS","COA","BIOLOGY"]
    }
]

key = input("Enter a specific key: ")

count = 0

for dict in list1:
    if(dict[key]):
        count += 1
    else:
        print(f"All dict is not having the key: {key}")


if count == len(list1):
    print(f"All dict is having the key: {key}")
else:
    print(f"All dict is not having the key: {key}")
    
