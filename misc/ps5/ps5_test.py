import itertools

#D = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]

#def loadData(f):
#    return [i.split(' ') for i in open(f, 'r').read().split('\n')][0], [i.split(' ') for i in open(f, 'r').read().split('\n')][1:-1]


def findDistanceXY(A, B):
    return ((float(A[0]) - float(B[0])) ** 2 + (float(A[1]) - float(B[1])) ** 2) ** 0.5

def findDistance(p, data):
    D = [[] for i in xrange(p)]

    #print D

    for i in xrange(p):
        #D[tuple(i, i)] = 0
        for j in xrange(p):
            A = data[i]
            B = data[j]

            D[i].append(int(findDistanceXY(A, B)))

    #for i in D:
    #   print i, D[i]

    return D


def solve_tsp_dynamic(p):
    #calc all lengths
    all_distances = p
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(p)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])

    return res

D = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10,4,8,0]]
#D = [[0, 2, 9, 10], [1, 0, 6, 4], [15,7, 0, 8], [6, 3, 12, 0]]
#D = [[float(x[0]), float(x[1])] for x in [x.split(' ') for x in open('tsp.txt').read().split('\n')][1:15]]
print D
#points = findDistance(len(D), D)
points = D

A = solve_tsp_dynamic(points)
print A
#1 -> 2 -> 4 -> 3 -> 1
#1 -> 4 -> 3 -> 2 -> 0
