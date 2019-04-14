
def rotLeft(a, d):
	n = len(a)
	rot = d
	
	return a[d:] + a[:d]
	

def rotLeftNaive(a, d):
	n = len(a)
	rot = d


	A = [0 for i in xrange(n)]

	for i in xrange(n):
		if i + rot >= len(a):
			rot_i = i + rot - len(a)
		else:
			rot_i = i + rot 
		
		A[i] = a[rot_i]


	return A

def testcases():
	d = 4
	a = [1, 2, 3, 4, 5]

	result = [5, 1, 2, 3, 4]

	print result == rotLeftNaive(a, d)
	print result == rotLeft(a, d)
	d = 3
	a = [1, 2, 3, 4, 5]

	result = [4, 5, 1, 2, 3]

	print result == rotLeft(a, d)

	a = "41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51"
	a = a.split(" ")

	d = 10
	result = "77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77"
	result = result.split(" ")

	print result == rotLeft(a, d)


if __name__ == '__main__':
	testcases()