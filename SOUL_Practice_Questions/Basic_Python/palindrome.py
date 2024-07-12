str1 = input("Enter a string: ")

list1 = list(str1)

list2 = list1.copy()

list2.reverse()

print(list1)
print(list2)

if(len(list1) == len(list2) and list1 == list2):
    print("Palindrome")
else:
    print("Not Palindrome")
