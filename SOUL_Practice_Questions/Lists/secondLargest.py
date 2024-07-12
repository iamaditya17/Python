# Write a program to find the second largest element in a list.

length = int(input("Enter the length of the list: "))

list1 = []

print("Enter the elements of list: ")

for i in range(length):
    ele = input()
    list1.append(ele)

list1.sort()

print(f"Second largest element is: {list1[1]}")
