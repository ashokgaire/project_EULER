"""
problem 7 



By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

def checkPrime(val):
    check = True
    for i in range(2,val):
        if val % i == 0:
            check = False
            break
        else:
            check = True
            
    return check

def Prime(n):
    a = 2
    primeList = []

    while len(primeList) < n:
        if checkPrime(a):
           
            primeList.append(a)
        a = a + 1
    print(primeList[n-1])


Prime(10001)

#104743