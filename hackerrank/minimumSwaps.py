def minimumSwaps(arr):
	cnt = 0 

	D = {value: key for key, value in enumerate(arr)}
	
	for i in xrange(len(arr) - 1):
		if i + 1 != arr[i]:
			value = i + 1
			key = D[value]
			#print arr[i], value

			D[value] = i
			D[arr[i]] = key

			arr[i], arr[key] = arr[key], arr[i]
		
			
			cnt += 1
		
	return cnt

def testcases():
	a = "4 3 1 2"
	a = map(int, a.split())
	result = 3

	print result == minimumSwaps(a)

	a = "2 3 4 1 5"
	a = map(int, a.split())
	result = 3
	print result == minimumSwaps(a)

	a = "1 3 5 2 4 6 7"
	a = map(int, a.split())
	result = 3
	print result == minimumSwaps(a)

	a = "7 1 3 2 4 5 6"
	a = map(int, a.split())
	result = 5
	print result == minimumSwaps(a)

if __name__ == '__main__':
	testcases()
	