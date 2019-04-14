def jumpingOnClouds(c):
	i = 0
	cnt = 0 

	while True:
		if i >= len(c) - 1:
			break
		elif i + 2 < len(c) and c[i + 2] == 0:
			cnt += 1
			i = i + 2
		elif i + 1 < len(c) and c[i + 1] == 0:
			cnt += 1
			i = i + 1

	return cnt

def testcases():
	n = 6
	c = [0, 0, 0, 0, 1, 0]
	result = 3
	print result == jumpingOnClouds(c)

	n = 6
	c = [0, 0, 1, 0, 1, 0]
	result = 3
	print result == jumpingOnClouds(c)

if __name__ == '__main__':
	testcases()