#Given a sorted array of integers arr and an integer num, 
#find all possible unique subsets of arr that add up to num. 
#Both the array of subsets and the subsets themselves should be 
#sorted in lexicographical order.

inc = 0

import itertools

def sumSubsets(arr, num):
	result = set()
	for i in xrange(1, len(arr) + 1):
		comb = itertools.combinations(arr, i)
		for c in comb:
			if sum(c) == num:
				result.add(c)

	print result 

	return sorted([list(i) for i in result]) if result != set([]) else [[]]

def sumSubsets3(arr, num):
	def findPermutations(arr):
		if arr == []:
			return set([tuple()])
		result = set()

		for j in xrange(len(arr)):
			val = arr[j]
			perms = findPermutations(arr[0:j] + arr[j+1:])
			
			for s in perms:
				if s != tuple():
					result.add(s)
				
				result.add(tuple([val]) + s)
			
		return result

	result = findPermutations(arr)
	finalResult = set()

	for comb in result:
		if sum(comb) == num:
			finalResult.add(tuple(sorted(comb)))

	finalResult = [list(i) for i in finalResult] 

	#print result
	return sorted(finalResult)


def sumSubsets2(arr, num):
	def findPermutations(arr):
		#print arr
		if arr == []:
			return [[]]
		result = []

		for j in xrange(len(arr)):
			val = arr[j]
			perms = findPermutations(arr[0:j] + arr[j+1:])
			
			for s in perms:
				result.append(s)
				result.append([val] + s)
			
			#print result

		return result

	result = findPermutations(arr)
	finalResult = set()

	for comb in result:
		if sum(comb) == num:
			finalResult.add(tuple(sorted(comb)))

	finalResult = [list(i) for i in finalResult]


	#print result
	return sorted(finalResult)

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
	num = 5
	arr = [1, 2, 3, 4, 5]

	result = [[1, 4], [2, 3], [5]]

	runTest(arr, num, result)

	num = 0
	arr = []

	result = [[]]

	runTest(arr, num, result)

if __name__ == '__main__':
	testcases()	
