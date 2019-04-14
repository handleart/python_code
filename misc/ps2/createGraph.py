def loadTestData2():
	arr = []
	p = []

	i = 0 
	with open('p1_test1.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0:

	    		tmp = line.strip().split()		
	    		p.append(tmp[0])
	    		p.append(tmp[1])
	    		arr.append(line.strip().split())

	    	i += 1



	return arr


result = loadTestData2()

for i in result:
	print '"' + i[0] + '" -> "' + i[1] + '" [ label="' + i[2] + '"];'

