

# pass statement [It is a null statement, not to do anything inside the loop]

for i in range(10):
    pass

print("Some useful work")

# WAP to find the sum of first n numbers

i = 1 
summ = 0
n = 5

while (i <= 10):
    if(i <= n):
        summ += i
        i += 1
    else:
        i += 1
        continue
print(summ)

# WAP to find the factorial of first n numbers

n = 5
i = 1
fact = 1

while (i <= n):
    fact *= i
    i += 1

print(fact)

#------Using for loop------

factorial = 1

for i in range(1,n+1):
    factorial *= i

print(factorial)


        



