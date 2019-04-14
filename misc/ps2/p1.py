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
		    		arr.append(line.strip().split())

		    	i += 1


	arr = sorted(arr, key = lambda y: y[2])

	return arr, set(p)


def loadTestData():

	x = []
	x.append(['1', '2', '3'])
	x.append(['1', '3', '3'])
	x.append(['2', '3', '4'])
	x.append(['3', '4', '7'])
	x.append(['4', '5' , '2'])

	x = sorted(x, key = lambda y: y[2])

	print x

	return x, set(['1', '2', '3', '4', '5'])

def loadTestData3():

	x = []
	x.append(['1', '2', '3'])
	x.append(['1', '3', '1'])
	x.append(['1', '4', '5'])
	x.append(['2', '4', '2'])
	x.append(['3', '4' , '4'])

	x = sorted(x, key = lambda y: int(y[2]))

	#print x

	return x, set(['1', '2', '3', '4'])

def loadTestData2():
	arr = []
	p = []

	i = 0 
	with open('p1_test1.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0:

	    		tmp = line.strip().split()		
	    		p.append(tmp[0])
	    		p.append(tmp[1])


	    		arr.append([tmp[0], tmp[1], int(tmp[2])])

	    	i += 1
	
	arr = sorted(arr, key = lambda y: y[2])
	print 'sorted', arr

	return arr, set(p)w

def loadTestData4():
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

def formatDataDict(inputData):
	f = {}

	for x in inputData:
		if x[2] not in f:
			f[x[2]] = []

		f[x[2]].append([x[0], x[1]])

	return f


def cluster(inputGraph, p, k):
	u = {}

	for i in p:
		u[i] = i

	

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
		



def cluster2(inputGraph, p, k):
	print 'start clustering'
	u = UnionFind.UnionFind()
	uTmp = UnionFind.UnionFind()

	for i in p:
		u.union(i)
		uTmp.union(i)

	T = u.parents.values()
	#print T

	inputGraph = sorted(inputGraph, key = lambda x: x[2])

	print 'parents', u.parents
	j = 0

	for i in inputGraph:
		j +=1
		
		print j, ":" , u[i[0]], u[i[1]], i[0], i[1]
		u.union(i[0], i[1])

		if j == 8:
			print u[i[0]], u[i[1]], u.parents
			break
		
		print 'parents', u.parents

		T = u.parents.values()
		print "T: ", set(T)

		if (len(set(T)) == k):
			print 'stop', k, len(set(T)), T
			break

			#print set(u.parents.values())

	print 'parents', u.parents

	G = []

	print u.parents

	for i in inputGraph:
		print 'test', i, u[i[0]], u[i[1]]

		if u[i[0]] != u[i[1]]:
			G.append(i[2])


	print G
	#return min(G)

actualData, p = loadData()
#testData, p = loadTestData()
#testData, p = loadTestData3()
testData, p = loadTestData4()


#result = cluster(testData, p, 2)
result = cluster(actualData, p, 4)

print result

#print result

#print testData
#print actualData[1:5]

