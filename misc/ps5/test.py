import itertools

f = 'tsp.txt'

def loadData(f):
	return [i.split(' ') for i in open(f, 'r').read().split('\n')][0], [i.split(' ') for i in open(f, 'r').read().split('\n')][1:5]

findDistanceXY = lambda A, B: ((float(A[0]) - float(B[0])) ** 2 + (float(A[1]) - float(B[1])) ** 2) ** 0.5
p, data = loadData(f)

all_distances = [[findDistanceXY(i, j) for i in data] for j in data]

all_distances = D = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]]

cnt = 4

all_distances = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]]
A = {(frozenset([0, i+1]), i+1): (dist, [0,i+1]) for i,dist in enumerate(all_distances[0][1:])}

print A
print '---'

for m in range(2, cnt):
    B = {}
    for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
        for j in S - {0}:
            B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
    A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    print A
    print res




