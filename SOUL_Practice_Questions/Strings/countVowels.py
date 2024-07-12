str1 = input("Enter a string: ")

list1 = list(str1)

count = 0

for ele in list1:
    if(ele.lower() in ('a','e','i','o','u',)):
        count += 1

print(f"No. of vowels present in {str1} are : {count}")