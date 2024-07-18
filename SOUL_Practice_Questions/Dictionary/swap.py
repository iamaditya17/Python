# Write a program to invert a dictionary, i.e., swap keys and values.

dict1 = {
    "name": "Aditya",
    "roll": 28,
    "sic": "20BECA21",
    "club": ["Cricket", "Football"]
}

# Ensure values are hashable before using them as keys in the inverted dictionary
# In this example, we assume all values are hashable; for non-hashable values, additional handling is needed.
inverted_dict = {}

for key, value in dict1.items():
    # Check if value is a list, convert it to a tuple
    if isinstance(value, list):
        value = tuple(value)
    inverted_dict[value] = key

print(inverted_dict)
