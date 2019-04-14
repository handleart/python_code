def miniMaxSum(arr):
	arr = sorted(arr)
	minVal = 0
	maxVal = 0
	
	for i in xrange(len(arr)):
		if i == len(arr) - 1:
			maxVal += arr[i]
		elif i == 0:
			minVal += arr[i]
		else:
			maxVal += arr[i]
			minVal += arr[i]

	print minVal, maxVal


a = [1, 2, 3, 4, 5]
output = miniMaxSum(a)

a = [5, 4, 3, 2, 1]
output = miniMaxSum(a)