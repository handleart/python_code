#!/usr/bin/python

def salesTotal(twoD_array):

	dict2d_array = {};

	for i in twoD_array:
		#print i, i[0], i[1]
		if i[0] in dict2d_array:
			dict2d_array[i[0]] += i[1];
		else:
			dict2d_array[i[0]] = i[1]

	return dict2d_array




tmp = [[211, 4], [262, 3], [211, 5], [216,6]];


print salesTotal(tmp);


