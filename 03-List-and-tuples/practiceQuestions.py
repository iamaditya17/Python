# WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []

print("Please enter your 3 favorite movies: ")

movie1 = input("Enter the 1st favorite: ")
movies.append(movie1)
movie2 = input("Enter the 2nd favorite: ")
movies.append(movie2)
movie3 = input("Enter the 3rd favorite: ")
movies.append(movie3)

print("Your favorite movies are:")

for i in range(0,len(movies)):
    print("Movie",i,": ",movies[i])

# WAP to check if a list contains palindrome of elements or not

list1 = [1,2,3,2,1]
list2 = list1.copy()

list2.reverse()
print(list2)

if(list1 == list2):
    print("Palindrome")
else:
    print("Not palindrome")

# WAP to count the no of students with the "A" grade in the follwing tuple

grades = ("A","B","C","A","B","D","A","A")

print(grades.count("A"))

# Store the above values in list and sort them

grades_list = list(grades)

grades_list.sort()

print(grades_list)