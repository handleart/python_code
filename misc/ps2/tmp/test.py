import itertools

i = 0 
arr = []
arrB = []
M = []

def cluster(inputGraph, p):
	u = {}

	for i in p:
		u[i] = i

	

	for i in inputGraph:
		T = set(u.values())
		#print len(T), k
		if len(T) <= k:
			break


		node0, node1 = i[0], i[1]

		#union(node0, node1)
		node0_k = u[node0]
		node1_k = u[node1]

		name = max(node0_k, node1_k)

		for z in u.keys():
			if u[z] == node0_k or u[z] == node1_k:
				u[z] = name

	G = []

	for i in inputGraph:
		#print 'edges left', i, u[i[0]], u[i[1]]

		if u[i[0]] != u[i[1]]:
			G.append(i[2])
			

	print min(G)

with open('file1.txt') as inputfile:
	    for line in inputfile:
	    	if i > 0 and i < 10:
	    		tmp = line.strip().replace(" ", "") 
	    		arrB.append(int(tmp, 2))
	    		arr.append(tmp)
	    	else:
	    		bitSize = line.strip().split()

	    	i += 1

#print 'arr', arr
#print set(arr)


f = '{0:0' + bitSize[1] + 'b}'
f = '{0:0' + '3' + 'b}'

oneBit = f.format(1)
twoBit = f.format(3)


#print ["".join(seq) for seq in itertools.product('01', repeat=3)]
x1 = set(["".join(seq) for seq in itertools.permutations(oneBit)])
x2 = set(["".join(seq) for seq in itertools.permutations(twoBit)])

#print set(["".join(seq) for seq in itertools.permutations('011')])

print 'x1', x1
z2 = []
z = []

setOfResults1 = []
setOfResults2 = []
nodes = []



for i in set(arr):
	for j in x1:
		#print '1', i, 'x', j, '=', '{0:03b}'.format(int(i, 2) ^ (int(j,2))), '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr

		if '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr:
			node0 = min([i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))])
			node1 = max([i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))])

			nodes.append(node0)
			nodes.append(node1)

			print node0, node1, [i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))]

			if [node0, node1] not in setOfResults1:
				setOfResults1.append([node0, node1])
				z.append([int(i, 2), int(j, 2), 1])

				

				z2.append(int(i, 2) ^ (int(j,2)))

		

	for j in x2:
		#print '2', i, 'x', j, '=', '{0:03b}'.format(int(i, 2) ^ (int(j,2))), '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr
		if '{0:03b}'.format(int(i, 2) ^ (int(j,2))) in arr:


			node0 = min([i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))])
			node1 = max([i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))])

			if [node0, node1] not in setOfResults1:
				setOfResults2.append([i, '{0:03b}'.format(int(i, 2) ^ (int(j,2)))])

				z2.append(int(i, 2) ^ (int(j,2)))
				z.append([int(i, 2), int(j, 2), 1])




#setOfResults = sorted(setOfResults, key=lambda x: x[2])

setOfResults1 = list(k for k,_ in itertools.groupby(setOfResults1))
setOfResults2 = list(k for k,_ in itertools.groupby(setOfResults2))


#print 's', setOfResults1
#print 's2', setOfResults2

#z = set(z)
#z2 = set(z2)

#print 'z', z
#print 'z2', z2
#print 'arr', arr

#for i in z2:
#	print i, '{0:03b}'.format(i)


intersect = set(z2).intersection(arrB)
difference = set(z2).difference(arrB)

print 'a', set(arrB)
print 'z2', set(z2)
print 'i', intersect
print 'd', difference

z = sorted(z, key = lambda x: x[2])

cluster(inputGraph)

#print set(arr)



