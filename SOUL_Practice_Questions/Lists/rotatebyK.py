# Write a Python program to rotate a list by k elements.

length = int(input("Enter the length of the list: "))

input_list = []

for i in range(length):
    ele = int(input())
    input_list.append(ele)

print("Original list: ",input_list)

k = int(input("Enter the no of elements you want to rotate"))

#run the loop for kth times
for i in range(k):
    input_list.insert(0,input_list.pop())  #pop the last element and add it to the 1st

print("After rotate list: ",input_list)