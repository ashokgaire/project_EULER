'''
problem 6

The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is,3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def sumOfSquare(n):
    sum = 0
    for i in range(n+1):
        sum += i*i

    return sum

def squareOfSum(n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum**2
        

def result(n):
    return squareOfSum(n) -sumOfSquare(n)

print(result(100))