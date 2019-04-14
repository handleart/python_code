#Analyze results from ps1 

fileNames = ['output_g3.txt']

def loadData(f):
	return [i.split(' ') for i in open(f, 'r').read().strip().split('\n')]


x = loadData(fileNames[0])
A = set()

for i in xrange(len(x)):
	for j in xrange(len(x[i])):
		A.add(int(x[i][j]))

print min(A)
#result is #-19
