def countSwaps(a):
	def swap(a, j):
		a[j], a[j + 1] = a[j + 1], a[j]

	def bubbleSort(a):
		swapCnt = 0
		for i in xrange(len(a) - 1):
			for j in xrange(len(a) - 1): 
			    if (a[j] > a[j + 1]):
			   		swap(a, j)
			   		swapCnt +=1

		return a, swapCnt

	return bubbleSort(a)	

def testcases():
	a = "3 2 1"
	a = map(int, a.split())
	print countSwaps(a)

	a = "4 4 1"
	a = map(int, a.split())
	print countSwaps(a)


if __name__ == '__main__':
	testcases()
	        
	    