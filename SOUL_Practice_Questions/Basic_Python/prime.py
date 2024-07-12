# WAP to check if a number is Prime or not. (a no which is divisible by 1 and itself)

num = int(input("Enter a number: "))

def isPrime(num):
    if(num <= 1):
        return False
    
    for i in range(2,num):
        if(num % i == 0):
            return False
    
    return True

if(isPrime(num)):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

