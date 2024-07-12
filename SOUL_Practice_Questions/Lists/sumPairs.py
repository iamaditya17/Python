length = int(input("Enter the length of the list: "))

list1 = []

print("Enter the elements of the list: ")

for i in range(length):
    ele = int(input())  # Convert input to integer
    list1.append(ele)

sum_pairs = {}

target_sum = int(input("Enter the sum: "))

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == target_sum:
            sum_pairs[(i,j)] = (list1[i], list1[j])

print("Pairs that sum up to", target_sum, "are:", sum_pairs)
