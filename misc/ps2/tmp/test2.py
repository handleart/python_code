import itertools
import numpy as np

def unique_permutations(elements):
    if len(elements) == 1:
        yield (elements[0],)
    else:
        unique_elements = set(elements)
        for first_element in unique_elements:
            remaining_elements = list(elements)
            remaining_elements.remove(first_element)
            for sub_permutation in unique_permutations(remaining_elements):
                yield (first_element,) + sub_permutation

def loadTetData2(m):
	arr = []
	p = {}

	i = 0 

	with open('../clustering_big.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0 and i <= m:
	    		tmp = line.strip().replace(" ", "") 
	    		arr.append(int(tmp, 2))
	    		p[int(tmp,2)] = int(tmp, 2)
	    	elif i == 0:
	    		bitSize = line.strip().split()
	    	else:
	    		break

	    	i += 1

	return set(arr), p, bitSize

arr, p, bitSize = loadTetData2(10)

bitSize = ['3', '24']

f = '{0:0' + bitSize[1] + 'b}'

oneBit = f.format(1)
print oneBit

twoBit = f.format(3)


x = unique_permutations(twoBit)

for i in x:
	print i









