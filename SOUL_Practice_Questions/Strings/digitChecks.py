# Write a program to check if a string contains only digits.

str1 = input("Enter a string: ")

def checkOnlyDigits(str):
    count = 0
    for i in range(0,len(str1)):
        if(str1[i].isdigit()):
            count += 1
        else:
            continue
    return count

checkCount = checkOnlyDigits(str1)

if(checkCount == len(str1)):
    print(f"{str1} contains only digits")
else:
    print(f"{str1} doesn't contain only digits")


        
    