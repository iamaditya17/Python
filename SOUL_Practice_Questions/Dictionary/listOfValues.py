# Write a Python program to extract a list of values associated with a specific key from a list of dictionaries.

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

for dict in list1:
    if(dict["subject"]):
        for sub in dict["subject"]:
            print(sub)

    else:
        print("No subject")