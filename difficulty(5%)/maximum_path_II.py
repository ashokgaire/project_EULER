

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

"""
def readData():
    triangle = [[0 for i in range(100)] for j in range(100)]
    with open("maximum_path_II.txt",'r') as data:
        j = 0
        for line in data:
                row = line.replace("\n","").split(" ")
                for i in range(len(row)):
                    triangle[j][i] = int(row[i])
                j +=1

    return triangle


def maxTotal(tri,n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):

            if tri[i+1][j] > tri[i+1][j+1]:
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]
    return tri[0][0]


ans = maxTotal(readData(),99)
print(ans)

