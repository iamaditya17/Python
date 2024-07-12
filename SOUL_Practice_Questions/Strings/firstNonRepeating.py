# Write a program to find the first non-repeating character in a string.

str1 = input("Enter a string: ")

def findFirstNonRepeating(str1):

    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str1:
        if char_count[char] == 1:
            return char


nonRepeatingChar = findFirstNonRepeating(str1)

print(nonRepeatingChar)



