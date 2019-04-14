

def kangaroo(x1, v1, x2, v2):

	#x1 + v1*t = x2 + v2*t
	#x1 - x2 = t * (v2 - v1)
	#(x1 - x2) / (v2 - v1) = t
	#

	if v2 < v1 and (x1 - x2) % (v2 - v1) == 0:
		result = 'YES'
	else:
		result = 'NO'

	print result
	return result






a = [0, 4, 5, 1]
x1 = a[0]
v1 = a[1]
x2 = a[2]
v2 = a[3]

result = 'YES'
output = kangaroo(x1, v1, x2, v2)
print result == output

a = [0, 2, 5, 3]
x1 = a[0]
v1 = a[1]
x2 = a[2]
v2 = a[3]

result = 'NO'
output = kangaroo(x1, v1, x2, v2)
print result == output

a = [1, 1, 0, 1]
x1 = a[0]
v1 = a[1]
x2 = a[2]
v2 = a[3]

result = 'NO'
output = kangaroo(x1, v1, x2, v2)
print result == output