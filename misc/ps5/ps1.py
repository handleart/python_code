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
	return [i.split(' ') for i in open(f, 'r').read().split('\n')][0], [i.split(' ') for i in open(f, 'r').read().split('\n')][1:-1]


def tsp(p, data):

	Z = []

	#A[tuple([s, 0])] = float('inf')


	

	C = {}
	C[tuple([0,0])] = 0

	D = findDistance(p, data)

	p = p -1
	
	#D = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]]
	#D = [[0, 1, 15, 6, 1], [2, 0, 7, 3, 2], [9, 6, 0, 12, 3], [10,4,8,0,4], [10,4,8,4,0]]
	#p = len(D)
	#print D[0]

	g = {}
	gg = {}

	for i in xrange(1,p):
		g[tuple([i,None])] = D[0][i]

	#print g

	s = itertools.combinations(xrange(1,p), 1)
	for j in s:
		for i in xrange(1,p):
			k = j[0]
			if i not in j:
				g[tuple([i,j])] = D[k][i] + g[tuple([k, None])]


	for m in xrange(2, p):
		print m
		
		s = itertools.combinations(xrange(1,p), m)

		for j in s:
			#print j
			for i in xrange(1,p):
				#k = j[0]
				#print 'not', i, j
				
				#print m, i, j
				if i not in j:
					#g[tuple([i, j])] = 0
					#find min of all the permutations of it
				
					f = itertools.combinations(j, m-1)

					#for xx in f:
					#	print j, xx

					
					for l in f:
						#print m, l, j
						z = []
						#print l	
						#print l, tuple([i, l]) in g
						v = set(j) - set(l)
						#print v
						#print j, l, i, v

						for k in v:
							#print tuple([i, j]), tuple([i, l]),  l, '-', k, i, '-', D[i][k], g[tuple([i, l])]
							#z.append(g[tuple([i, l])] + D[i][k])
							

							if tuple([i, j]) not in g:
								g[tuple([i, j])] = g[tuple([k, l])] + D[k][i]
							elif g[tuple([i, j])] > g[tuple([k, l])] + D[k][i]:
								g[tuple([i, j])] = g[tuple([k, l])] + D[k][i]

						

							if tuple([i, j]) not in gg:
								gg[tuple([i, j])] = []

							gg[tuple([i, j])].append(['i', i, 'l', l, 'k', k, 'tuple', tuple([i, l]), g[tuple([k, l])], D[k][i]])



	
	j = tuple(range(1,p))
	f = itertools.combinations(j, p-2)

	for l in f:
		z = []
		#print l	
		#print l, tuple([i, l]) in g
		v = set(j) - set(l)

		#print m, l, j, v
		#print v
		#print v
		#print j, l, i, v

		i = 0

		for k in v:
			#print tuple([i, j]), tuple([i, l]),  l, '-', k, i, '-', D[i][k], g[tuple([i, l])]
			#z.append(g[tuple([i, l])] + D[i][k])			

			if tuple([i, j]) not in g:
				g[tuple([i, j])] = g[tuple([k, l])] + D[k][i]
			elif g[tuple([i, j])] > g[tuple([k, l])] + D[k][i]:
				g[tuple([i, j])] = g[tuple([k, l])] + D[k][i]

		

			if tuple([i, j]) not in gg:
				gg[tuple([i, j])] = []

			gg[tuple([i, j])].append(['i', i, 'l', l, 'k', k, 'tuple', tuple([i, l]), g[tuple([k, l])], D[k][i]])


	print '--'
	for i in gg:
		print i, gg[i]

	print '--'
	for i in g:
		print i, g[i]
	#for m in xrange(p):
	#	for 

	#return min(data)

def findAllSubsets(g, j):

	return 0

def findDistanceXY(A, B):
	return ((float(A[0]) - float(B[0])) ** 2 + (float(A[1]) - float(B[1])) ** 2) ** 0.5

def findDistance(p, data):
	D = [[] for i in xrange(p)]

	#print D

	for i in xrange(p):
		#D[tuple(i, i)] = 0
		for j in xrange(p):
			A = data[i]
			B = data[j]

			D[i].append(findDistanceXY(A, B))

	#for i in D:
	#	print i, D[i]

	return D

p, data = loadData(f)

#print len(data)
#print p, data

#print findDistance(int(p[0]), data)
tsp(int(p[0]), data)
#print tsp(int(p[0]), data)

'''
--

(3, (1, 2)) 12
(2, (1, 3)) 20
(1, (2, 3)) 17
(3, None) 6
'''

