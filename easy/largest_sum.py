'''

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

'''



with open("data.txt","r") as file:
    data = [int(line.strip()) for line in file]

print(str(sum(data))[:10])