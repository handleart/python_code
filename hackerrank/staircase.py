def staircase(n):
	for i in xrange(n):
		f = []
		for j in xrange(1, n + 1):
			if n - j <= i:
				f.append('#')
			else:
				f.append(' ')
		
		print "".join(f)


if __name__ == '__main__':
    n = 6

    staircase(n)