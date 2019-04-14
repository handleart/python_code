'''
This problem also asks you to solve a knapsack instance, but a much bigger one.
Download the text file here. This file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

'''

import datetime

def loadData():
	return [i.split(' ') for i in open('knapsack_big.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('knapsack_big.txt', 'r').read().split('\n')][1:-1]

def loadTestDataSmall():
	return [i.split(' ') for i in open('k_test1.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('k_test1.txt', 'r').read().split('\n')][1:-1]

def loadTestDataLarge():
	return [i.split(' ') for i in open('k_test2.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('k_test2.txt', 'r').read().split('\n')][1:-1]


def knapsack(size, data):
	A = [0 for i in xrange(int(size[0]) + 1)]

	B = A[:]

	W = int(size[0])
	V = int(size[1])

	#print V, W

	
	for i in xrange(1,V+1):

		w_i = int(data[i - 1][1])

		for x in xrange(W,0, -1):
			v_i = int(data[i - 1][0])

			if w_i  <= x:
				B[x] = max([B[x], B[x-w_i] + v_i])
				B[x] = 0
			else:
				B[x] = B[x]



	return B[-1]


size, data = loadTestDataSmall()

#print size, data

x = knapsack(size, data)
print x, 'answer should be: ', '8'

#larger test data
size, data = loadTestDataLarge()

#print size, data

x = knapsack(size, data)
print x, 'answer should be: ', '1398904'
t = datetime.datetime.now()

#larger test data
size, data = loadData()

#print size
print "load actual data"



print t

x = knapsack(size, data)

t1 = datetime.datetime.now()

print t1, t1 - t

print ""
print x, 'answer should be: ', '?'

t2 = datetime.datetime.now()

print t2, t2 - t1