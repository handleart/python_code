import json
import sys

BOARD_SIZE = 8

def under_attack(col, queens):
    x = y = col

    for r, c in reversed(queens):
        x , y = x - 1, y + 1 #check for the prev queen location 

        if c in (x , col, y):
            return True
    return False

def solve(n): # n is the number of queens to be placed
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution+[(n,i+1)]
        for i in xrange(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)] #call the function 

former, sys.stdout = sys.stdout, open('queen.txt','w')

for answer in solve(BOARD_SIZE):
    print answer

results, sys.stdout = sys.stdout, former #former is used for ip & op
print json.dumps(answer) #dumps is used to write in json file