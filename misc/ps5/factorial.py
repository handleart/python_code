import itertools

tmp = 1
val = 4

A = []

for i in xrange(1,val+1):
	tmp = tmp * i



for j in xrange(1,val):
	tmp2 = itertools.combinations(xrange(val), j)

	
	for i in tmp2:
		A.append(i)

print A
print len(A)