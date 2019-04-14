def diagonalDifference(arr):
	diff = 0
	for i in xrange(len(arr)):
		end = len(arr) - 1 - i
		diff -= arr[i][i] - arr[i][end]
	return abs(diff)

a = [[11, 2, 4],
	  [4, 5, 6],
	 [10, 8, -12]]

print diagonalDifference(a)
