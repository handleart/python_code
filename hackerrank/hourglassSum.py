def hourglassSum(arr):
	hourglass = [[-1, -1], [-1, 0], [-1, 1],
				       [0,  0],
			 [1, -1],  [1,  0], [1, 1]]
			 
	result = float('-inf')
	A = []
	for y in xrange(1,len(arr)-1):
		for x in xrange(1,len(arr[y]) -1) :
			tmp = 0
			for h in hourglass:
				y0 = h[0]
				x0 = h[1]
				#print y + y0, x + x0, arr[y + y0][x + x0] 
				tmp += arr[y + y0][x + x0] 
			#A.append(tmp)
			if tmp > result:
				result = tmp
		#print A
		#print result

	return result

def testcases():
	A = [[-9, -9, -9,  1, 1, 1], 
		 [0, -9,  0,  4, 3, 2],
		 [-9, -9, -9,  1, 2, 3],
		 [0,  0,  8,  6, 6, 0],
		 [0,  0,  0, -2, 0, 0],
		 [0,  0,  1,  2, 4, 0]]

	result_actual = [[-63, -34, -9, 12], 
					 [-10, 0, 28, 23], 
					 [-27, -11, -2, 10], 
					 [9, 17, 25, 18]]

	final_result = 28

	print final_result == hourglassSum(A)

if __name__ == '__main__':
	testcases()