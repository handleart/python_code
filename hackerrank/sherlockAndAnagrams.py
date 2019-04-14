from itertools import combinations 

def sherlockAndAnagrams(s):
	x = set()
	result = 0
	for i in xrange(len(s)):
		for j in combinations(s, i):
			if set(sorted(j)) in x:
				result += 1
			else:
				x.add(sorted(j))
			#print x
	print result
	return 0

def testcases():
	s = "abba"
	result = 4

	print result == sherlockAndAnagrams(s)

	s = "abcd"
	result = 0


	print result == sherlockAndAnagrams(s)

	s = "ifailuhkqq"
	result = 3

	print result == sherlockAndAnagrams(s)

	s = "kkkk"
	result = 10

	print result == sherlockAndAnagrams(s)

if __name__ == '__main__':
	testcases()