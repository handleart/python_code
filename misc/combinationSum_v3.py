#Given an array of integers a and an integer sum, 
#find all of the unique combinations in a that add up to sum.
#The same number from a can be used an unlimited number of times in a
# combination.
#Elements in a combination (a1 a2 ... ak) must be sorted in 
#non-descending order, while the combinations themselves 
#must be sorted in ascending order.
#If there are no possible combinations that add up to sum, the output should be the string "Empty".

import itertools

inc = 0

def flattenList(l):
		#print 'l', l, D
		s = [[]]
		for item in l:	
			if debug: print 'DItem', D[item], len(D[item])
			if len(D[item]) == 1:
				for i in s:
					#print 'i', i, D[item], i + D[item][0]
					i += D[item][0]
			else:
				tmpS = []
				for i in D[item]:
					
					for j in s:
						tmpS.append(j + i)

				s = tmpS

			
			#s = sorted(s)
		print 's', [sorted(i) for i in s]
		return [sorted(i) for i in s]

def combinationSum(a, total, debug = False):
	result = []
	def combinationSumHelper(l, r, sumArr, sumTot = 0): 
		val = sum(l[0])
		#val = l[0]
		#sumTot = sumTot - val

		if sumArr + val == total:
			result.append(r + [1] + [0 for i in xrange(len(l) - 1)])
			#if debug: print 'result', result

		if sumArr + val > total:
			return False

		if val > total:
			return False

		if len(l) > 1:
			combinationSumHelper(l[1:], r + [1], sumArr + val, 0)
			combinationSumHelper(l[1:], r + [0], sumArr, 0)


	D = {}
	#if debug: print a, total

	for i in a:
		maxVal = total / i
		#if debug: print i, 'maxVal', maxVal
		for y in xrange(1, maxVal + 1):
			if y * i not in D:
				D[y * i] = []
			
			D[y * i].append([i for z in xrange(y)])

	S = []

	if D == {}:
		return "Empty"

	for i in sorted(D.keys()):
		S.extend(D[i])

	#print 'S', S
	combinationSumHelper(S, [], 0, sum(D.keys()))
	if debug: print a
	
	if debug: print 'D', D
	
	result = [[x * y for x, y in zip(i, S) if x * y != []] for i in result]
	if debug: print result
	#result = [[x * y for x, y in zip(i, D.keys()) if x * y != 0] for i in result]
	#print result
	#print 'r1',result
	solution = set()
	for i in result:
		solution.add(tuple(sorted(itertools.chain.from_iterable(i))))

	#print solution
	
	string = ''

	for s in sorted(solution):
		tmpString = "(" + " ".join(map(str, s)) + ")"
		if tmpString not in string:
			string += tmpString
	if debug: print 'str', string

	return string if string != '' else 'Empty'

	

def runTest(a, s , expectedResult):
	#print 'Passed' if result == findSubstrings(words, parts) else 'Failed'
	global inc
	inc += 1

	print inc
	
	output = combinationSum(a, s) #longestPath(t)

	#print "result:", expectedResult, "output:", output

	if expectedResult == output:
		print 'Passed' 
	else:
		print 'Failed'
		print '----'
		print 'Expected result', expectedResult
		#output = sumSubsets(n, True)

		print 'output', combinationSum(a, s, True)
		exit()


	print '---'


def testcases():
	a = [2, 3, 5, 9]
	s = 9

	result =  "(2 2 2 3)(2 2 5)(3 3 3)(9)"
	#				8      9      9    9 

	runTest(a, s, result)

	a = [2, 4, 6, 8]
	s = 8
	result = "(2 2 2 2)(2 2 4)(2 6)(4 4)(8)"

	runTest(a, s, result)


	a = [8, 1, 8, 6, 8]
	s = 12
	result = "(1 1 1 1 1 1 1 1 1 1 1 1)(1 1 1 1 1 1 6)(1 1 1 1 8)(6 6)"
	runTest(a, s, result)

	a = [7, 2, 6, 5]
	s = 16
	result = "(2 2 2 2 2 2 2 2)(2 2 2 2 2 6)(2 2 2 5 5)(2 2 5 7)(2 2 6 6)(2 7 7)(5 5 6)"

	runTest(a, s, result)

	a = [6, 5, 7, 1, 8, 2, 9, 9, 7, 7, 9]
	s = 6
	result = "(1 1 1 1 1 1)(1 1 1 1 2)(1 1 2 2)(1 5)(2 2 2)(6)"

	runTest(a, s, result)

	a = [5, 2, 2, 6]
	s = 3
	result = "Empty"

	runTest(a, s, result)

	a = [4, 6, 4, 2]
	s = 7
	result = "Empty"

	runTest(a, s, result)

	a = [8, 7, 1]
	s = 22
	result = "(1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1)(1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 7)(1 1 1 1 1 1 1 1 1 1 1 1 1 1 8)(1 1 1 1 1 1 1 1 7 7)(1 1 1 1 1 1 1 7 8)(1 1 1 1 1 1 8 8)(1 7 7 7)(7 7 8)"

	runTest(a, s, result)

	a = [6, 5, 5, 7]
	s = 1
	result = "Empty"

	runTest(a, s, result)



if __name__ == '__main__':
	testcases()	