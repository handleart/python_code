def repeatedString(s, n):
	length = len(s)
	occurence = n % length
	cnt = 0 
	cntOccurence = 0

	for i in xrange(len(s)):
		if i < occurence and s[i] == 'a':
			cntOccurence += 1

		if s[i] == 'a':
			cnt += 1

	#print cntOccurence, cnt, n / length, cntOccurence + cnt * (n / length)
	return cntOccurence + cnt * (n / length)



def testcases():
	s = 'faaab'
	n = 3
	result = 2
	print result == repeatedString(s, n)

	s = 'aba'
	n = 10
	result = 7
	print result == repeatedString(s, n)

	s = 'aba'
	n = 1
	result = 1
	print result == repeatedString(s, n)

	s = 'a'
	n = 1000000000000
	result = 1000000000000
	print result == repeatedString(s, n)

	s = 'abaa'
	n = 4
	result = 3
	print result == repeatedString(s, n)

if __name__ == '__main__':
	testcases()
