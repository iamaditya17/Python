str1 = input("Enter a string: ")

def countFrequency(str1):

    chardict = {}

    for char in str1:

        if char in chardict:    #if the character is already there in the dict then increment it's value by 1
            chardict[char] += 1
        else:
            chardict[char] = 1

    return chardict

frequency_dict = countFrequency(str1)

for char,frequency in frequency_dict.items():
    print(f"'{char}' : {frequency}")


    