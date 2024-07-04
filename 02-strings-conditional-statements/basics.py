# Escape sequence characters

str1 = "Hii Aditya.\nHow are you?"  # \n will shift to the new line
print(str1)

str2 = "Hii Aditya.\tHow are you?"  # \t will add a tab space
print(str2)

# String Concatenation
str1 = "Hello"
str2 = "World"

print(str1 + str2)
print(len(str1))

#indexing (readOnly and write operation is not allowed)

name = "Aditya Patra"
print(name[0])

#Slicing (It is used to access a speific part of a string)

collegeName = "Silicon University"

print(collegeName[0:7]) #collegeName[starting_index:n-1]
print(collegeName[8:]) # when we didn't give any last range value then python will bydefault consider upto last (len(collegeName))

# Silicing (Backward counting: where the last letter is taken as -1 then second last is -2 ......)

collegeName = "Silicon University"

print(collegeName[::-1]) # reverse [start: end: step:-1]

#capitalize() [will capitalize string's 1st letter]

name1 = "aditya"
print(name1.capitalize())

#endswith("ya") [check the given string ends with "ya" or not] if yes: True no: False

print(name1.endswith("ya"))

#replace(old,new) [replace all the occurances of old with new]

name2 = name1.replace('adi','Adi')
print(name2)

#find(word) [return 1st index of the word if the word is available in the string]  index starting from 0.

str4 = "Hi Aditya how are you?"
print(str4.find("how"))

#count(word) [count the occurance of the specific word in a given string]

str5 = "AAAABBCDE"
print(str5.count('A'))