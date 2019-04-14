'''

Question 3:
In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. 
This file describes an undirected graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. 
You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. 

You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. 

OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. 

The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). 

The superior approach stores the unprocessed vertices in the heap, as described in lecture. 

Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

'''

import random

def prims(input_data, s):

	X = set()
	V = set(input_data.keys())
	X.add(s)

	E = {}
	E[0] = []
	E[1] = []

	cost = 0 

	#print input_data

	for v in input_data[s]:
		if v[0] not in X:
			E[0].append(v[0])
			E[1].append(v[1])

	#print '-'

	j = 0
	#print s

	while True:
		j +=1

		#print X, V, E, 
		index_min = E[1].index(min(E[1]))
		

		#print len(E[0]), len(E[1]), index_min
		s = E[0].pop(index_min)
		cost += E[1].pop(index_min)

		X.add(s)

		#print 's', s, 'cost:', cost, 'E', E, 'i', index_min, 'X', X, 'V', V
		

		while s in E[0]:
			index = E[0].index(s)

			E[0].pop(index)
			E[1].pop(index)




		#print indices

		for v in input_data[s]:
			#print v
			if v[0] not in X:
				#print 'v', v
				E[0].append(v[0])
				E[1].append(v[1])
	

		if X == V:
			break

	return cost



def randomize_prims(input_data):

	#all_nodes = list(set(input_data[0] + input_data[1]))
	all_nodes = input_data.keys()
	val = []


	for i in xrange(20):
		#s = 1
		s = all_nodes[random.randint(0, len(all_nodes) - 1 ) ]
	
		val.append(prims(input_data, s))


	print set(val)



	#prims(input_data, s)


def run_script():

	edges = []
	edges_dict = {}
	all_nodes = []

	node0 = []
	node1 = []
	cost = []

	i = 0

	with open('edges.txt') as inputfile:
	    for line in inputfile:
	    	#if i >1 and i < 10:
	    	if i >1:
	    		node0Tmp = int(line.strip().split()[0])
	    		node1Tmp = int(line.strip().split()[1])

	    		#node0.append(node0Tmp)
	    		#node1.append(node1Tmp)

	    		costTmp = int(line.strip().split()[2])

	    		#cost.append(int(line.strip().split()[2]))

	    		if node0Tmp not in edges_dict:
	    			edges_dict[node0Tmp] = []

	    		if node1Tmp not in edges_dict:
	    			edges_dict[node1Tmp] = []



	    		edges_dict[node0Tmp].append([node1Tmp, costTmp])
	    		edges_dict[node1Tmp].append([node0Tmp, costTmp])




	    		#print node0, node1, line

	    		

	    		#if 

	    		#edges.append(line.strip().split())

	    	i += 1


	#print edges_dict

	randomize_prims(edges_dict)


def test_script():
	edges_dict = {}

	edges_dict[1] = [[2, 2], [4,1]]
	edges_dict[2] = [[1, 2], [4,2]]
	edges_dict[3] = [[4, 3]]
	edges_dict[4] = [[1,1], [2,2], [3, 3]]




	randomize_prims(edges_dict)

#test_script()
run_script()
#result is -3612829


