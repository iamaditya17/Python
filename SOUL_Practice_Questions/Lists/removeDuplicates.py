# Write a program to remove duplicates from a list.

length = int(input("Enter the length of the list: "))

input_list = []

for i in range(length):
    ele = int(input())
    input_list.append(ele)

input_list.sort()

unique_list = []

for i in range(len(input_list)):
    if i == 0 or (input_list[i] != input_list[i-1]):
        unique_list.append(input_list[i])
    

print(unique_list)