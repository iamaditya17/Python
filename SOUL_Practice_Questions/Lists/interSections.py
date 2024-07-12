# Write a Python program to find the intersection of two lists.

len1 = int(input("Enter the length of list1: "))
len2 = int(input("Enter the length of list2: "))

list1 = []
list2 = []

list3 = []

print("Enter the elements of list1: ")
for i in range(len1):
    ele = input()
    list1.append(ele)

print("Enter the elements of list2: ")
for i in range(len2):
    ele = input()
    list2.append(ele)

for i in range(len(list1)):
    for j in range(len(list2)):
        if(list1[i] == list2[j]):
            list3.append(list1[i])
        else:
            continue

print("Common elements are: ",list3)