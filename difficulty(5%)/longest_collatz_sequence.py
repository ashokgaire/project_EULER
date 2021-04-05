"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million

"""


number = 1000000

sequenceLength = 0
startingNumber = 0
cache = [None]*(number+1)

for i in range(len(cache)):
    cache[i] = -1

cache[1] = 1

for i in range(2,number):
    sequence = i
    k = 0
    while(sequence !=1 and sequence >=i):
        k+=1
        if sequence % 2 == 0:
            sequence = sequence/2
        else:
            sequence = sequence*3 +1

    
    cache[i] = k + cache[int(sequence)]

    if(cache[i] > sequenceLength):
        sequenceLength = cache[i]
        startingNumber = i

print(startingNumber, sequenceLength)