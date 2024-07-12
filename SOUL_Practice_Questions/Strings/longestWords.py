# Write a program to find the longest word in a string.

str1 = input("Enter a string: ")

word = str1.split(" ")

largestWord = word[0]

for i in range(len(word) -1):
    if(len(word[i]) <= len(word[i+1])):
        largestWord = word[i+1]
    else:
        largestWord = word[i]

print(f"Largest word is : {largestWord}")