# Write a program to check if two strings are anagrams.

# 2 strings are said to be anagrams if both contains same element but the order can be different. Length of both should be same.

str1 = input("Enter String1: ")
str2 = input("Enter String2: ")

list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

print(list1)
print(list2)

def checkAnagram():
    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False
    return True
        
if(checkAnagram()):
    print("Strings are anagrams!!!")
else:
    print("Strings are not anagrams!!!")


#-----------OR-----------------

if(len(str1) == len(str2)):
    if(sorted(str1) == sorted(str2)):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")