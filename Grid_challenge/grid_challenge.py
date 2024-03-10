import math
import os
import random
import re
import sys


def gridChallenge(grid):
    # Write your code here
    
    for x in range(0,len(grid)-1):
        for y in range(len(grid[x])):
            if sorted(grid[x])[y]>sorted(grid[x+1])[y]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
