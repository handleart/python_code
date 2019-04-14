def twoStrings(s1, s2):
	s1 = set(s1)
	s2 = set(s2)

	if s1 - s2 == s1:
		return "NO"
	else:
		return "YES"

def testcases():
	s1 = "hello"
	s2 = "world"
	print twoStrings(s1, s2)

	s1 = "hi"
	s2 = "world"
	print twoStrings(s1, s2)

if __name__ == '__main__':
    testcases()