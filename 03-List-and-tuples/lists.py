marks = [10,20,30,40,50,60,70,80,90,100]

print(marks[0])

print(type(marks))

#Length of list
print(len(marks))

#append() [used to add a new element into list at last]

marks.append(45)
print(marks)

#reverse() [It will reverse the entire list]

marks.reverse()
print(marks)

#sort() [It will sort the list in ascending order]
marks.sort()
print(marks)

print(marks.sort(reverse=True)) # It will sort the list in reverse order

#count() [It will count the no of occurance of an elements present in the list]
print(marks.count(10))

#copy() [It will copy the entire list]
marks1 = marks.copy()
print("New copied list is: ",marks1)

#index() [It will return the index of a particular element of the list]
print(marks.index(45))

#insert(index,ele) [it will add the element at the specified index]

marks.insert(5,48)
print(marks)

#pop() [It will remove the element from the last]
marks1.pop()
print(marks1)

#pop(index)  [It will delete the element at the given index]
marks.pop(4)
print(marks)

#clear() [It is used to delete the entire list]
marks1.clear()
print("New list: ",marks1)

#remove() [It is used to remove an specific element from the list (only remove element's 1st occurance)]
marks.remove(90)    # it will remove 90 from list marks 
print(marks)

#extend()  [It is used to append any list,set or tuples to the existing list]

name = ("Aditya","Ayush","Siddharth","Tushar")
marks.extend(name)

print(marks)  # O/P: [10, 20, 30, 40, 45, 50, 60, 70, 80, 100, 'Aditya', 'Ayush', 'Siddharth', 'Tushar']

#list slicing

# syntax: list_name[starting_index : ending_index]

print(marks[0:])  #print 0th index to the last
print(marks[1:5]) #print 1st index to 5th index (print till 4th index)
print(marks[:4])   #print 0th index to 4th
print(marks[-3:-1])  #print -3 index to -1(which is last element)