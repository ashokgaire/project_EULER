""" 
Multiple of 3 and 5 


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

#########    O(1) time method 

LIMIT=99999999999999999999999999999999999999999999999999999999999999999999999

# Get the upper bounds for the arithmetic series
upper_for_three = LIMIT // 3
upper_for_five = LIMIT // 5
upper_for_fifteen = LIMIT // 15

# calculate sums
sum_three = 3*upper_for_three*(1 + upper_for_three) / 2
sum_five = 5*upper_for_five*(1 + upper_for_five) / 2
sum_fifteen = 15*upper_for_fifteen*(1 + upper_for_fifteen) / 2

# calculate total
total = sum_three + sum_five - sum_fifteen

print(int(total))



