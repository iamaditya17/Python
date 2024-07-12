collection = {1,2,2,2,3,4,4}

print(collection)  #{1,2,3,4} bcuz it will not consider the duplicates

#Empty set

set1 = set()
print(type(set1))

#add(ele) [It will add an element to the set]
# we can add any type of data except list and dict bcuz it's immutable

collection.add(5)
print(collection) 

#remove(ele)  [It will remove the given element from the set]

collection.remove(5)
print(collection)

#clear()  [remove all elements from the set]

collection.clear()
print(collection)

collection1 = {1,1,1,2,2,2,3,3,3,4,4}

#pop()  [remove random value from set]

collection1.pop()
print(collection1)

#set1.union(set2) [take the unique elements from both the set and then perform union]

set2 = {1,2,2,3,3,3,4,4,4,4}
set3 = {2,3,4,4,4,4,5}

print(set2.union(set3))  #{1,2,3,4,5}

#set1.intersection(set2)  [take the unique elements from both the set and returns the common elements from both]

print(set2.intersection(set3)) #{2,3,4}