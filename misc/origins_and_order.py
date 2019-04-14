#!/usr/bin/python

import itertools

def answer(x,y,z):
	#your code here
	#print x, y, z:

	valid_months = xrange(1,13)
	for i in valid_months:
		print i

	valid_days = {}

	#valid days per month
	valid_days[1] = valid_days[3] = valid_days[5] = valid_days[7] = valid_days[8] = valid_days[10] = valid_days[12] = 31
	valid_days[4] = valid_days[6] = valid_days[9] = valid_days[11] = 30;

	#no leap years
	valid_days[2] = 28

	comb = set(itertools.permutations([x, y, z]))
	print comb

	valid_comb = []

	for i in comb:
		month = i[0]
		day = i[1]
		year = i[2]

		if month in valid_months:
			if day <= valid_days[month]:
				valid_comb.append(i)

		#don't need to go on if the value is larger than 0
		#if len(valid_comb) > 1:
		#	break

	if len(valid_comb) > 1:
		return valid_comb
		#return "Ambiguous"
	elif len(valid_comb) == 0:
		return "Error"
	else:
		return '{:02d}'.format(valid_comb[0][0]) + '/' + '{:02d}'.format(valid_comb[0][1]) + '/' + '{:02d}'.format(valid_comb[0][2])



z = itertools.combinations(xrange(1,100), 3)

f = []
print answer(12,31,12)


#for i in z:
	#print answer(i[0], i[1], i[2])
