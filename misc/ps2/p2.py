'''


In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. 
So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.
The data set is here. The format is:
[# of nodes] [# of bits for each node's label]
[first bit of node 1] ... [last bit of node 1]
[first bit of node 2] ... [last bit of node 2]
...
For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits ---
between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the
label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? That is,
how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. 
So you will have to be a little creative to complete this part of the question. 
For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?


'''

import itertools

def loadTetData1():
	arr = []
	p = {}

	i = 0 

	with open('tmp/file1.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0:
	    		tmp = line.strip().replace(" ", "") 
	    		arr.append(int(tmp, 2))
	    		p[int(tmp,2)] = int(tmp, 2)
	    	else:
	    		bitSize = line.strip().split()

	    	i += 1
	return set(arr), p, bitSize

def loadTetData2(m):
	arr = []
	p = {}

	i = 0 

	with open('clustering_big.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0 and i <= m:
	    		tmp = line.strip().replace(" ", "") 
	    		arr.append(int(tmp, 2))
	    		p[int(tmp,2)] = int(tmp, 2)
	    	elif i == 0:
	    		bitSize = line.strip().split()
	    	else:
	    		break

	    	i += 1

	return set(arr), p, bitSize

def loadData():
	arr = []
	p = {}

	i = 0 

	with open('clustering_big.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0:
	    		tmp = line.strip().replace(" ", "") 
	    		arr.append(int(tmp, 2))
	    		p[int(tmp,2)] = int(tmp, 2)
	    	elif i == 0:
	    		bitSize = line.strip().split()
	    	else:
	    		break

	    	i += 1

	return set(arr), p, bitSize

def unique_permutations(elements):
	if len(elements) == 1:
	    yield (elements[0],)
	else:
	    unique_elements = set(elements)
	    for first_element in unique_elements:
	        remaining_elements = list(elements)
	        remaining_elements.remove(first_element)
	        for sub_permutation in unique_permutations(remaining_elements):
	            yield (first_element,) + sub_permutation

def cluster(arr, p, bitSize):
	f = '{0:0' + bitSize[1] + 'b}'
#f = '{0:0' + '3' + 'b}'

	oneBit = f.format(1)
	twoBit = f.format(3)



	#x1 = set([int("".join(seq),2) for seq in itertools.permutations(oneBit)])
	#x2 = set([int("".join(seq),2) for seq in itertools.permutations(twoBit)])
	#x1 = itertools.permutations(oneBit)
	#x2 = itertools.permutations(twoBit)

	


	print "Starting Job"

	#print 'x1', x1

	setOfResults = []
	setOfResults1 = []
	costArr = {}
	costArr[1] = []
	costArr[2] = []
	participants = []

	x1 = unique_permutations(oneBit)

	for k in x1:
		

		for i in arr:
		
		
				

		
			j = int("".join(k),2)
			#print 1, i, f.format(j), 'x', "".join(k), '=', f.format(i ^ j), i, j, i ^ j

			#print '1', i, 'x', j, '=', '{0:03b}'.format(int(i, 2) ^ (int(j,2))), '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr
			if i ^ j in arr:
				node0 = min([i ^ j, i])
				node1 = max([i ^ j, i])

				if [node0, node1] not in setOfResults:
					setOfResults.append([node0, node1])
					setOfResults1.append([node0, node1, 1])
					costArr[1].append([node0, node1])
					participants.append(node0)
					participants.append(node1)

		
		
		#print 'x2'

	x2 = unique_permutations(twoBit)
	
	for k in x2:

		for i in arr:
			#print '1', i, 'x', j, '=', '{0:03b}'.format(int(i, 2) ^ (int(j,2))), '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr
			j = int("".join(k),2)
			#print 'h', i, j

			#print 2, i, f.format(j), 'x', "".join(k), '=', f.format(i ^ j), i, j, i ^ j

			if i ^ j in arr:
				node0 = min([i ^ j, i])
				node1 = max([i ^ j, i])

				if [node0, node1] not in setOfResults:
					setOfResults.append([node0, node1])
					setOfResults1.append([node0, node1, 1])
					
					costArr[2].append([node0, node1])

					participants.append(node0)
					participants.append(node1)



	print "Created cost"
	#print 'cost', costArr

	intersect = set(participants).intersection(arr)
	difference = set(participants).difference(arr)

	Y = len(difference)

	print 'Calcualting costs'

	#print 'cost', costArr.keys()
	#print p

	#now cluster
	
	print len(setOfResults1)

	z = set(participants)



	print len(p), len(participants)
	

	for i in setOfResults1:

				node0, node1, cost = i[0], i[1], i[2]

				node0_k = p[node0]
				node1_k = p[node1]


				name = max(node0_k, node1_k)

				p[node0_k] = name
				p[node1_k] = name

				
				

	
	



	print "Test Result = ", Y, Y + len(set(p.values()))
	

print 'test1'

arr, p, bitSize = loadTetData1()
print arr
f = '{0:0' + bitSize[1] + 'b}'
for i in arr:
	print f.format(i), i


print 'test2'

cluster(arr, p, bitSize)

arr, p, bitSize = loadTetData2(1000)

print "Starting Cluster"

cluster(arr, p, bitSize)

#print 'test3'


arr, p, bitSize = loadTetData2(10000)
cluster(arr, p, bitSize)

#print "Starting Cluster"


print 'Running Actual'


#arr, p, bitSize = loadData()
#print "Starting Cluster"

#cluster(arr, p, bitSize)





