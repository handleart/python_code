#Test Case 1 

visited = []

def answer(population, x, y, strength):
    for i in range(len(population)):
        arr =  [False] * len(population[0]) 
        visited.append(arr)


    print visited
    #infect(population, x, y, strength)
    infect_iter(population, x, y, strength)
    return(population)



def infect(population, x, y, strength):
    if visited[x][y] == False:
        visited[x][y] = True;
        if population[x][y] <= strength:
            population[x][y] = -1;

            neighbors = findNeighbors(population, x, y)

            for n in neighbors:
                if visited[n[0]][n[1]] == False:
                    infect(population, n[0], n[1], strength);
    

def infect_iter(population, x, y, strength):
    q = [[x,y]]; 
    len_x = len(population)
    len_y = len(population[0])

    while q:

        a, b = q.pop();

        if visited[a][b] != True:
            visited[a][b] = True

            if population[a][b] <= strength:
                population[a][b] = -1;

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


def findNeighbors(population, x, y):
    len_x = len(population)
    len_y = len(population[0])
    neighbors = []

    if x - 1 >= 0 and x - 1 < len_x:
        neighbors.append([x-1, y])

    if x + 1 >= 0 and x + 1 < len_x:
        neighbors.append([x+1, y])

    if y - 1 >= 0 and y - 1 < len_y:
        neighbors.append([x, y - 1])

    if y + 1 >= 0 and y + 1 < len_y:
        neighbors.append([x, y + 1])

    return neighbors

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

    for i in xrange(51):
        population.append([])
        for j in xrange(51):
            population[i].append(random.randrange(0,10000))


    #print f 

    #The Strength and Resistance values will be between 0 and 10000. 
    #The population grid will be at least 2x2 and no larger than 50x50. The x and y values will be valid indices in the population arrays, with numbering beginning from 0.

    x = 0;
    y = 0;
    strength = 8000;

    ans = answer(population, x, y, strength);
    print ans

def test_simple():
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

    print "Pass", (result == ans)
    print "Answer: " + str(ans)

#test1()
#print "----"
test2()
#print "----"
#test3()
#print "----"
#test4()