#Given a sorted array of integers arr and an integer num, 
#find all possible unique subsets of arr that add up to num. 
#Both the array of subsets and the subsets themselves should be 
#sorted in lexicographical order.

inc = 0


def sumSubsets(arr, num):
	A = [] 
  	def sumSubsetsHelper(a, sumArr, sumTot, p, debug = False):
 		if a == []:
 			return []

 		val = a.pop(0)
 		if sumArr > num: 
 			return False

 		if val > num:
 			return False

 		newSumTot = sumTot - val
 		newSumArrAdd = sumArr + val
 		newSumArrSub = sumArr

  		if newSumArrAdd == num:  			
  			p = p + [1]

  			if len(p) != len(arr):
  				for i in xrange(len(arr) - len(p)):
  					p += [0]

  			A.append(p)
  		
  		else:
  			left = sumSubsetsHelper(a[:], newSumArrAdd, newSumTot, p + [1])
  			right = sumSubsetsHelper(a[:], sumArr, newSumTot, p + [0])


  	sumTot = sum(arr)

  	if sumTot >= num:
  		sumSubsetsHelper(arr[:], 0, sumTot, [])

  	result = set()
  	for r in A:
  		result.add(tuple([a*b for a,b in zip(arr, r) if b != 0]))
  	
  	return sorted([list(i) for i in result]) if result != set() else [[]]
  	
#return sorted(finalResult) if finalResult != [] else [[]]

def runTest(arr, num, expectedResult):
	#print 'Passed' if result == findSubstrings(words, parts) else 'Failed'
	global inc
	inc += 1

	print inc
	

	output = sumSubsets(arr, num) #longestPath(t)

	#print "result:", expectedResult, "output:", output

	if expectedResult == output:
		print 'Passed' 
	else:
		print 'Failed'
		print '----'
		print 'Expected result', expectedResult
		#output = sumSubsets(n, True)

		print 'output', output


	print '---'

def testcases():
	arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]
	num = 9
	result = [[1,1,1,1,1,1,1,1,1]]
	runTest(arr, num, result)

	num = 3
	arr = [1, 2, 3, 4, 5]

	result = [[1,2], [3]]

	runTest(arr, num, result)


	num = 5
	arr = [1, 2, 3, 4, 5]

	result = [[1, 4], [2, 3], [5]]

	runTest(arr, num, result)
 	


	num = 0
	arr = []

	result = [[]]

	runTest(arr, num, result)

	num = 10
	arr = range(1, 51)

	result = [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [1, 9], [2, 3, 5], [2, 8], [3, 7], [4, 6], [10]]

	runTest(arr, num, result)

	num = 2
	arr = range(3, 51)

	result = [[]]

	runTest(arr, num, result)

	num = 5
	arr = [1, 2, 2, 3, 4, 5]
	result = [[1,2,2], [1,4], [2,3], [5]]

	runTest(arr, num, result)



if __name__ == '__main__':
	testcases()	
