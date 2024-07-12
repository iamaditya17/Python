# FWAP to find a substring is present inside a string or not

str1 = input("Enter a string: ")

def findSubstring(substr):

    for i in range(len(str1) - len(substr) + 1):
        if((str1[i:len(substr) + i]) == substr):
            print(f"{substr} found at position {i}")
            break
        else:
            continue

substr = input("Enter a substring: ")

findSubstring(substr)


#--------Or(using inbuilt function)---------

if(str1.find(substr) == 1):
    print("Present")
else:
    print("Not present")