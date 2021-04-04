"""
problem 10



The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import math
def checkPrime(val):
  
    for i in range(2,int(math.sqrt(val))+1):
        if val % i == 0:
            return False
            
            
    return True
            
 

def Prime(n):
    a = 2
    sum = 0

   
    for i in range(2,n):
        if checkPrime(i):
            sum = sum + i
    return sum


print(Prime(2000000))

        

