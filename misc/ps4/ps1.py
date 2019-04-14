'''
Question 1
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files 
describing three graphs: graph #1; graph #2; graph #3.

The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge 
(the first two numbers are its tail and head, respectively) and its length (the third number).
 NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. 
For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute minu,v - Vd(u,v), 
where d(u,v) denotes the shortest-path distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, 
then enter the length of its shortest shortest path in the box below. 

If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, 
try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: If you want a bigger data set to play with, try computing the shortest shortest path for this graph.

For g3.txt
the shortest path for vertex 1 is -7
the shortest path for vertex 10 is -3
the shortest path for vertex 20 is -9
the shortest path for vertex 30 is -9
'''

import thread
import multiprocessing
import timeit

#Floyd Warshall algorithm
#Johnson's algorithm
fileNames = ['g1.txt', 'g2.txt', 'g3.txt']
testFileNames = ['test.txt', 'test2.txt']

#return V (number of vertices), g (graph) based on input file name in the expected format
def loadData(n):
	#return [i.split(" ") for i in open(n, 'r').read().split('\n')][0], [i.split(" ") for i in open(n, 'r').read().split('\n')][1:-1]
	return [i.split(" ") for i in open(n, 'r').read().split('\n')][0], [i.split(" ") for i in open(n, 'r').read().split('\n')][1:-1]



def floydWarshall_simple(V, g):



	A = [float('inf') for i in xrange(V)]
	B =  [A[:] for i in xrange(V)]

	for i in xrange(V):
		B[i][i] = 0
	
	#print 'g', g
	#print B

	for i in g:
		S = int(i[0]) - 1 #Source
		D = int(i[1]) - 1 #Dest
		C  = int(i[2]) #Cost

		B[S][D] = C


	print 'B1', B

	for k in xrange(V):
		for i in xrange(V):
			for j in xrange (V):
				
				B[i][j] = min(B[i][j], B[i][k] + B[k][j])

				print j, i, k, 'A', B[i][j], 'B', B[i][k], 'C', B[k][j], 'min', min(B[i][j], B[i][k] + B[k][j])

	

	#print 'B', B
	return B


def floydWarshall_tuple(V, g):
	dist = {}

	for i in g:
		S = int(i[0]) #Source
		D = int(i[1]) #Dest
		C  = int(i[2]) #Cost

		name = tuple([S, D])

		dist[name] = C

	#print dist

	for i in xrange(1,V+1):
		name = tuple([i, i])
		dist[name] = 0

	print 'created graph tuple format'

	#Y = [float('inf') for i in xrange(V)]
	#Z =  [Y[:] for i in xrange(V)]


	#for i in dist:
	#	Z[i[0] - 1][i[1] -1] = dist[i]


	#print 'z', Z

	for k in xrange(1,V+1):
		print k, timeit.timeit() 
		for i in xrange(1, V+1):
			for j in xrange (1, V+1):
				#B[i][j] = min(B[i][j], B[i][k] + B[k][j])

				name1 = tuple([i, j])
				name2 = tuple([i, k])
				name3 = tuple([k, j])

				if name1 in dist:
					A =  dist[name1]
				else:
					A = float('inf')

				if name2 in dist:
					B = dist[name2]
				else:
					B = float('inf')

			
				if name3 in dist:
					C = dist[name3]
				else:
					C = float('inf')
	

				name4 = tuple([i, i])

				if dist[name4] != 0:
					print "negative cycle"
					return dist 
					
				dist[name1] = min(A, B + C)
				 
				#print k, i, j, 'A', A, 'B', B, 'C', C, 'min', min(A, B+C)



			#test = tuple([i, i])
			#if dist[test] < 0:
			#	print "negative cycle"
			#	return 0


				#continue

	return dist

def floydWarshall_dict(V, g):
	graph = {}

	for i in g:
		#print i

		S = int(i[0]) #Source
		D = int(i[1]) #Dest
		C  = int(i[2]) #Cost

		if S not in graph:
			graph[S] = {} 

		graph[S][D] = C


	dist = {}

	for u in graph:
		dist[u] = {}

		for v in graph:
			dist[u][v] = float('inf')

		dist[u][u] = 0

		for neighbor in graph[u]:
			dist[u][neighbor] = graph[u][neighbor]



	for t in graph:
		for u in graph:
			for v in graph:
				newdist = dist[u][t] + dist[t][v]
				if newdist < dist[u][v]:
					dist[u][v] = newdist
	    

	print dist

def runJob(f):
	print 'loaded data'
	V, g = loadData(f)
	V = int(V[0])
	#V = 100

	'''
   	print V
   	print g


   	#x = floydWarshall(int(V[0]), g[0:100])
   	x1 = floydWarshall(V, g)
  

   	x2 = floydWarshall2(V, g)

	A = [float('inf') for i in xrange(V)]
	B =  [A[:] for i in xrange(V)]

	for i in x2:
		B[i[0] - 1][i[1] -1] = x2[i]

	print 'Result A', x1
	print 'Result B', B

	
	'''

	print 'starting floyd warshall'
	x2 = floydWarshall_tuple(V, g)


	print 'finished floyd warshall'

	#V = 1000
	
	A = [float('inf') for i in xrange(V)]
	B =  [A[:] for i in xrange(V)]

	for i in x2:
		B[i[0] - 1][i[1] -1] = x2[i]


	print "writing to file"
	outputFile = open('output_' + f, 'w')


	for i in xrange(V):
		if B[i][i] != 0:
			outputFile.write("negative cycle")
			return 0
	

	for i in B:
		#for j in i:
		outputFile.write("%s\n" %" ".join(map(str, i)))
			#outputFile.write("%s " %j)
	
		#outputFile.write("\n")

	print 'done with', f


if __name__ == "__main__":
	p = multiprocessing.Pool(3)
	p.map(runJob, fileNames)
	#p.map(runJob, testFileNames)
	#runJob('test2.txt')
   	#print 'x2', x2
	#result = bellmanFord(int(V[0]), g[1])





