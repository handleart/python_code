def minimumBribes(q):
	result = 0
	
	for pos, v in enumerate(q):
		val = v - 1

		if val - pos > 2: 
			return "Too chaotic"
	
		for j in range(max(val - 1, 0),pos):
			#print pos, val, val - 1, j
			if q[j] > val:
				result += 1

	return result

def testcases():
	q = "2 1 5 3 4"
	q = map(int, q.split())
	print minimumBribes(q)

	q = "2 5 1 3 4"

	q = map(int, q.split())
	print minimumBribes(q)

	q = "5 1 2 3 7 8 6 4"
	q = map(int, q.split())
	print minimumBribes(q)


	q = "1 2 5 3 7 8 6 4"
	q = map(int, q.split())
	print minimumBribes(q)

	q = "1	5	4	3	2	6"
	q = map(int, q.split())
	print q
	print minimumBribes(q)
if __name__ == '__main__':
    testcases()