"""
problem 4 


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit number
"""


def checkPalindrome(value):
    return str(value) == str(value)[::-1]

def palindrome():
    a = {}
    for i in range(0,1000):
        for j in range(0,1000):
            c = i * j
           
            if checkPalindrome(c):
                a[c] = str(i) +"*"+ str(j)
    return a


result = palindrome()
print(max(result))

