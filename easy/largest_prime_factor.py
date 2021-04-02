
"""
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def primefactor(n):
    if n < 0 :
        return
    p = 2
    PF = []
    while True:
        if n >= p ** 2:
            if n % p == 0:
                n = n/p
                PF.append(p)
                
            else:
                p +=1
        else:
            PF.append(int(n))
            break
    return PF
    

result = primefactor(600851475143)
print(max(result))



