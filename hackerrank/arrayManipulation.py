def arrayManipulation(n, queries):
	a = [0 for i in xrange(n + 1)]
	maxVal = 0

	for q in queries:
		start = q[0] - 1
		end = q[1]
		val = q[2]

		a[start] += val
		a[end] -= val

		#print a

	result = []
	last = 0
	maxVal = 0 

	for i in a:
		val = last + i
		if val > maxVal:
			maxVal = val
		result.append(val)
		last = val

	#print a, result
	return maxVal

def testcases():
	nm = "5 3"
	n = int(nm.split()[0])
	m = int(nm.split()[1])

	queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
	result = 200

	print result == arrayManipulation(n, queries)

	n = 10

	queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
	result = 10
	print result == arrayManipulation(n, queries)

	n = 10
	queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
	result = 31
	print result == arrayManipulation(n, queries)
	#print arrayManipulationNaive(n, queries)
    


if __name__ == '__main__':
	testcases()