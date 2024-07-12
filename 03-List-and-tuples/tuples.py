tup = (1)
print(type(tup))  #this will return int bcuz if our tuple contains single element then put a "," at the end so that it will take this as a tuple 

#index(ele)  [It will return the index of the given element (1st occurance)]

tup1 = (1,2,3,4,5,6,1,2,3,4,5,6)

print(tup1.index(2))

#count(ele) [It will return the count of occurance of the given element]

print(tup1.count(6))
