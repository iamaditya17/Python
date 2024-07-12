# Greatest common divisor among 2 numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

def gcd(num1,num2):

   gcd = 1

   for i in range(1,min(num1,num2)+1):
    if(num1 % i == 0 and num2 % i == 0):
       gcd = i

   return gcd
   

findGcd = gcd(num1,num2)

print(f"gcd of {num1} and {num2} is {findGcd}")


