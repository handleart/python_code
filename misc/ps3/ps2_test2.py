'''
In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here. This file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

'''

def loadData():
	return [i.split(' ') for i in open('knapsack1.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('knapsack1.txt', 'r').read().split('\n')][1:-1]

def loadTestDataSmall():
	return [i.split(' ') for i in open('k_test1.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('k_test1.txt', 'r').read().split('\n')][1:-1]

def loadTestDataLarge():
	return [i.split(' ') for i in open('k_test2.txt', 'r').read().split('\n')][0], [i.split(' ') for i in open('k_test2.txt', 'r').read().split('\n')][1:-1]


def knapsack(size, data):
	A = [0 for i in xrange(int(size[0]) + 1)]
	B = [A[:] for i in xrange(int(size[1]) + 1)]


	

	W = int(size[0])
	V = int(size[1])

	#print V, W

	for i in xrange(1,V+1):
		w_i = int(data[i - 1][1])
		

		for x in xrange(W,0,-1):
			v_i = int(data[i - 1][0])


			if w_i  <= x:
				B[i][x] = max([B[i-1][x], B[i-1][x-w_i] + v_i])
			else:
				B[i][x] = B[i-1][x]



	return B[-1][-1]


size, data = loadTestDataSmall()

print size, data

x = knapsack(size, data)
print x, 'answer should be: ', '8'

#larger test data
size, data = loadTestDataLarge()

print size, data

x = knapsack(size, data)
print x, 'answer should be: ', '1398904'


#larger test data
size, data = loadData()

print size

#load actual data

x = knapsack(size, data)
print x, 'answer should be: ', '2493893'
