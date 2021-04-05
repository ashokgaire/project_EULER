"""
problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


# Recursive soluton
cache = {}
def countRoutes(m,n):
    if n == 0 or m == 0:
        return 1

    if (m,n) in cache.keys():
        return cache[(m,n)]
    cache[(m,n)] = countRoutes(m,n-1) + countRoutes(m-1,n)
    return cache[(m,n)]
#print(countRoutes(20,20))

# Iterative Solution O(mxn) time

def countRoute(m,n):
    grid = [[0 for i in range(m+1)] for j in range(n+1)]
    

    for i in range(0,m+1):
        grid[i][0] = 1

    for j in range(0,n+1):
        grid[0][j] = 1
    print(grid)
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m][n]

#print(countRoute(3,3))


##########   Combinatorial Solution  O(n) time and O(1) space

# m = n for perfect grid
def Count(n):
    result = 1

    for i in range(1,n+1):
        result = result *(n+i)/i

    print(result)

Count(20)



