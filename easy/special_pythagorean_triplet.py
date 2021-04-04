"""
problem 9



A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def checkTheorem(a,b,c):
    return a**2 + b**2 == c**2

def condition(a,b,c):
    return a < b < c


def checkSum(a,b,c):
    return a+b+c == 1000

def find():
    sum = 1000
    product = 0
    for a in range(1,sum//3):
        for b in range(a+1,sum//2):
            c = sum -a -b
            if checkTheorem(a,b,c):
                print(a,b,c)
                product = a * b *c
    return product


                
print(find())
