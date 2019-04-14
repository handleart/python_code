def birthdayCakeCandles(ar):
	maxVal = ar[0]
	cnt = 0

	for i in ar:
		if i > maxVal:
			maxVal = i
			cnt = 1
		elif i == maxVal:
			cnt += 1

	print cnt


a = [3, 2, 1, 3]
birthdayCakeCandles(a)
