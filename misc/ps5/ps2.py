'''
Question 1
In this assignment you will implement one or more algorithms for the traveling salesman problem, 
such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance. 
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates 
the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- 
that is, two cities at locations (x,y) and (z,w) have distance sqrt((x-z)2+(y-w)2)  between them.


In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.
OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here. 
The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. 
What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

HINT: You might experiment with ways to reduce the data set size. 
For example, trying plotting the points. Can you infer any structure of the optimal solution? 
Can you use that structure to speed up your algorithm?
'''

import itertools

f = 'tsp.txt'

def loadData(f):
	return [i.split(' ') for i in open(f, 'r').read().split('\n')][1:-1]


def tsp(data):
	p = len(data)
	A = {(frozenset([0, i + 1]), i + 1): (dist, [0,i + 1]) for i, dist in enumerate(data[0][1:])}

	print A

	for m in xrange(2, p):
		B = {}
		for S in [frozenset(s) | {0} for s in itertools.combinations(xrange(1,p), m)]:
			for i in S - {0}:
				#print m, [(A[(S-{i},k)][0] + data[k][i], A[(S - {i}, k)][1] + [i]) for k in S if k != 0 and k != i]
				
				B[(S, i)] = min([(A[(S-{i},k)][0] + data[k][i], A[(S - {i}, k)][1] + [i]) for k in S if k != 0 and k != i])
				
		A = B

		print min([(A[d][0] + all_distances[d[1]][0], A[d][1]) for d in A])
		
		#result = min


data = loadData(f)

print data
asa
#data = data[0:1]

findDistanceXY = lambda A, B: ((float(A[0]) - float(B[0])) ** 2 + (float(A[1]) - float(B[1])) ** 2) ** 0.5
all_distances = [[findDistanceXY(i, j) for i in data] for j in data]

#all_distances = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]]

tsp(all_distances)

'''
--

(3, (1, 2)) 12
(2, (1, 3)) 20
(1, (2, 3)) 17
(3, None) 6
'''

