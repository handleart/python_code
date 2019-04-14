#!/usr/bin/python

import itertools

tmp = []
for i in xrange(1,1001): 
	tmp.append( i ) ;
#tmp.sort()

myDict = {}

for i in tmp:
	for j in tmp:
		z = sorted([i, j]);
		index = i ** 3 + j ** 3
		if index in myDict:
			if z not in myDict[index]:
				myDict[index].append(z)
		else:
			myDict[index] = [];
			myDict[index].append(z);


print len(myDict)

i = 0
cubeRootTmp = {};

for tmp in myDict:
	if len(myDict[tmp]) > 1:
		print myDict[tmp]

