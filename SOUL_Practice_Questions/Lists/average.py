# Write a Python program to find the average of elements in a list.

length = int(input("Please enter the length of the list: "))

input_list = []

for i in range(length):
    ele = int(input(f"Please enter the {i+1} elements of list: "))
    input_list.append(ele)

sum = 0
count = 0

for i in range(len(input_list)):
    count += 1
    sum += input_list[i]

average = sum / count

print(f"Average is: {average}")
