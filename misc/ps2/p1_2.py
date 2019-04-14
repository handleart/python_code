'''
In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. 

Download the text file here. 

This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
[number_of_nodes]
[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
...
There is one edge (i,j) for each choice of 1<=i<j<=n, where n is the number of nodes. For example, the third line of the file is "1 3 5250", 
indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. 

You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. 

What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

'''

import heapq
import UnionFind
import copy

def loadData():
	arr = []
	p = []

	i = 0 
	with open('clustering1.txt') as inputfile:
		    for line in inputfile:
		    	if i > 0:
		    		
		    		tmp = line.strip().split()		
		    		p.append(tmp[0])
		    		p.append(tmp[1])
		    		arr.append([tmp[0], tmp[1], int(tmp[2])])

		    	i += 1


	arr = sorted(arr, key = lambda y: y[2])

	return arr, set(p)


def loadTestData():
	arr = []
	p = []

	i = 0 
	with open('p1_test2.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0:

	    		tmp = line.strip().split()		
	    		p.append(tmp[0])
	    		p.append(tmp[1])


	    		arr.append([tmp[0], tmp[1], int(tmp[2])])
	    	#else:
	    		#p = xrange(1, int(line.strip())+1)
	

	    	i += 1
	
	arr = sorted(arr, key = lambda y: y[2])
	print 'sorted', arr

	return arr, set(p)

def cluster(inputGraph, p, k):
	u = {}

	for i in p:
		u[i] = i

	#print u
	
	#return 0

	for i in inputGraph:
		T = set(u.values())
		#print len(T), k
		if len(T) <= k:
			break


		node0, node1 = i[0], i[1]

		#union(node0, node1)
		node0_k = u[node0]
		node1_k = u[node1]

		name = max(node0_k, node1_k)

		for z in u.keys():
			if u[z] == node0_k or u[z] == node1_k:
				u[z] = name

	G = []

	for i in inputGraph:
		#print 'edges left', i, u[i[0]], u[i[1]]

		if u[i[0]] != u[i[1]]:
			G.append(i[2])
			

	print min(G)
		


actualData, p = loadData()
#testData, p = loadTestData()
#testData, p = loadTestData3()
testData, p2 = loadTestData()


result = cluster(testData, p2, 2)
result = cluster(actualData, p, 4)


#print result

#print testData
#print actualData[1:5]

