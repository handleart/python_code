def firstDuplicate(a):
	D = {}

	for indx, val in enumerate(a):
		if val in D:
			return val
		else:
			D[val] = [indx]

	return -1

def firstDuplicate2(a):


	
	

a = [2, 3, 3, 1, 5, 2]
print firstDuplicate(a) == 3

a = [2, 4, 3, 1, 5, 2]
print firstDuplicate(a) == 2

a = [2, 4, 3, 5, 5, 2]
print firstDuplicate(a) == 5

a = [5, 2, 3, 5, 5, 2]
print firstDuplicate(a) == 5

a = [1, 2, 3, 4, 5, 6]
print firstDuplicate(a) == 0