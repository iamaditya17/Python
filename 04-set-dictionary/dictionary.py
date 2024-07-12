#In python dictionary contains key value pairs and the values of the key can be a list,set or dictionary also.

#get(key)  [It will return the value of the given key]

studentDetails = {
    "name": "Aditya",
    "cgpa": 9.05,
    "marks": [90,96,98]
}

print("CGPA: ",studentDetails["cgpa"])

print("Name: ",studentDetails.get("name"))

# It is mutable

studentDetails["cgpa"] = 9.06  #chnage the cgpa value from 9.05 to 9.06

studentDetails["Address"] = "BBSR"  # will add a new key value

print(studentDetails)

#Nested Dictionary

student = {
    "name": "Aditya",
    "score": {
        "math": 90,
        "phy": 94,
        "chem": 96
    },
    "branch": "CST"
}

print(student["score"]["math"])

#keys() [It will return all the keys of the dictionary]

print(student.keys())

#values() [It will return all the values of the keys present in the dictionary]

print(student.values())

#items() [It will return all (key,val) pairs as tuples]

print(student.items())

#update(newDict) [It will insert the specified items to the dictionaries]

student.update({
    "city": "BBSR"
})

print(student)

#len(dicitonary_name)  [return the no. of key value present in the outerlayer [not include nested]]

print(len(student))

#fromkeys(keys)  [returns a dictionary with the specified keys and it's value, if no value given bydefault will take 0]

x = ('key1','key2','key3')
y = 0

thisDict = dict.fromkeys(x,y)

print(thisDict)  #{'key1': 0, 'key2': 0, 'key3': 0}
