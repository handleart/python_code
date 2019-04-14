def sockMerchant(n, ar):
	s = set()
	pair = 0
	for i in xrange(n):
		if ar[i] in s:
			pair += 1
			s.remove(ar[i])
		else:
			s.add(ar[i])

	return pair


def testcases():
	n = 9
	arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
	result = 3
	print result == sockMerchant (n, arr)

	n = 2
	arr = [1, 1]
	result = 1
	print result == sockMerchant (n, arr)

	n = 1
	arr = [1]
	result = 0
	print result == sockMerchant (n, arr)

if __name__ == '__main__':

    testcases()