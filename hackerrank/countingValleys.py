def countingValleys(n, s):
	cnt = 0
	elevation = 0
	lastElevation = 0

	for i in xrange(n):	
		if s[i] == 'U':
			lastElevation = elevation
			elevation += 1
		elif s[i] == 'D':
			lastElevation = elevation
			elevation -= 1

		if elevation == 0 and lastElevation < 0:
			cnt += 1

		#print s[i], elevation, lastElevation, cnt 

	#print 'cnt', cnt
	return cnt

def testcases():
	n = 8
	s = 'UDDDUDUU'
	result = 1
	print result == countingValleys(n, s)

	n = 8
	s = 'DDUUUUDD'
	result = 1
	print result == countingValleys(n, s)

	n = 3
	s = 'DUD'
	result = 1
	print result == countingValleys(n, s)

	n = 3
	s = 'UDU'
	result = 0
	print result == countingValleys(n, s)

if __name__ == '__main__':
	testcases()

