
import itertools

x = 'AABACC'

y = itertools.permutations(x)

print len(set(y))

for i in y:
	print i