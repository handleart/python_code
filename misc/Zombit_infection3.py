#!/usr/bin/python

def answer(population, x, y, strength):
    len_y = len(population);
    len_x = len(population[0]) 

    visited = []
    for i in range(len_y):
        tmp =  [False] * len_x
        visited.append(tmp)

    #print population
    #print visited

    q = [[x, y]]; 

    while q:
        a, b = q.pop();
        #print a, b

        if visited[b][a] != True:
            visited[b][a] = True

            if population[b][a] <= strength:
                population[b][a] = -1;

                i, j = a - 1, b
                if i >= 0 and i < len_x:
                    q.append([i, j])

                i, j = a + 1, b
                if i >= 0 and i < len_x:
                    q.append([i, j])

                i, j = a, b - 1
                if j >= 0 and j < len_y:
                    q.append([i, j])

                i, j = a, b + 1
                if j >= 0 and j < len_y:
                    q.append([i, j])


    return population

def test1():
    population = [[1, 2, 3], 
                  [2, 3, 4],
                  [3, 2, 1]];

    x = 0;
    y = 0;
    strength = 2;

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])
    print population

    ans = answer(population, x, y, strength);

    result = [[-1, -1, 3], 
              [ -1,  3, 4],
              [  3,  2, 1]];

    print "Pass", (result == ans)
    print "Answer: " + str(ans)

def test2():

    population = [[6, 7, 2, 7, 6],
                  [6, 3, 1, 4, 7], 
                  [0, 2, 4, 1, 10], 
                  [8, 1, 1, 4, 9], 
                  [8, 7, 4, 9, 9]];

    x = 2;
    y = 1;
    strength = 5;
    result = [[ 6,  7, -1,  7, 6],
               [ 6, -1, -1, -1, 7], 
               [-1, -1, -1, -1, 10], 
               [ 8, -1, -1, -1, 9], 
               [ 8,  7, -1,  9, 9]];

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])

    ans = answer(population, x, y, strength);

    print "Pass", (result == ans)
    print "Pop   : " + str(result)
    print "Answer: " + str(ans)

def test3():
    population = [[6, 7, 2, 7, 6],
                  [6, 3, 1, 4, 7], 
                  [0, 2, 4, 1, 10], 
                  [8, 1, 1, 4, 9], 
                  [8, 7, 4, 9, 9]];

    x = 4;
    y = 4;
    strength = 5;


    result = [[6, 7, 2, 7, 6],
              [6, 3, 1, 4, 7], 
              [0, 2, 4, 1, 10], 
              [8, 1, 1, 4, 9], 
              [8, 7, 4, 9, 9]];

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])

    ans = answer(population, x, y, strength);

    print "Pass: ", (result == ans)
    print "Pop   : " + str(result)
    print "Answer: " + str(ans)

def test4():
    population = [[1, 2], 
                  [2, 3]];

    x = 0;
    y = 0;
    strength = 2;

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])
    print population

    ans = answer(population, x, y, strength);

    result = [[-1, -1], 
              [-1, 3]];

    print "Pass: ", (result == ans)
    print "Pop   : " + str(result)
    print "Answer: " + str(ans)

def test_perf():
    import numpy as np 
    import random

    #population = np.random.randint(10000, size = (50,50));

    population = []

    for i in xrange(1000):
        population.append([])
        for j in xrange(500):
            population[i].append(random.randrange(0,10000))


    #print f 

    #The Strength and Resistance values will be between 0 and 10000. 
    #The population grid will be at least 2x2 and no larger than 50x50. The x and y values will be valid indices in the population arrays, with numbering beginning from 0.

    x = 0;
    y = 0;
    strength = 8000;

    ans = answer(population, x, y, strength);

    

    

def test5():
    population = [[1, 2, 3], 
                  [2, 3, 4],
                  [3, 2, 1]];

    x = 0;
    y = 0;
    strength = 10;

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])
    print population

    ans = answer(population, x, y, strength);

    result = [[-1, -1, -1], 
              [-1 ,-1, -1],
              [-1, -1, -1]];

    print "Pass", (result == ans)
    print "Answer: " + str(ans)

def test6():

    population = [[6, 7, 2, 7, 6],
                  [6, 3, 1, 4, 7], 
                  [0, 2, 4, 1, 10], 
                  [8, 1, 1, 4, 9], 
                  [8, 7, 4, 9, 9]];

    x = 4;
    y = 4;
    strength = 5;
    result = [[6, 7, 2, 7, 6],
                  [6, 3, 1, 4, 7], 
                  [0, 2, 4, 1, 10], 
                  [8, 1, 1, 4, 9], 
                  [8, 7, 4, 9, 9]];

    print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[x][y])

    ans = answer(population, x, y, strength);

    print "Pass", (result == ans)
    print "Pop   : " + str(result)
    print "Answer: " + str(ans)

def test7():

    population = [[6, 7, 2, 7, 6],
                  [6, 3, 1, 4, 7]];

    x = 2;
    y = 1;
    strength = 5;
    result = [[6, 7, -1, 7, 6],
              [6, -1, -1, -1, 7]];

    #print "Starting Point: " + str(x) + "," + str(y) + ": " + str(population[y][x])

    ans = answer(population, x, y, strength);

    print "Pass", (result == ans)
    print "Pop   : " + str(result)
    print "Answer: " + str(ans)

test1()
print "test1 ----"
test2()
print "test2 ----"
test3()
print "test3 ----"
test4()
print "test4 ----"
test_perf()
print "test5 ----"
test5()
print "test6 ----"
test6()
print "test 7 ----"
test7()