arg = ["".join(x.split(' ')) for x in open('clustering_big.txt', 'r').read().split('\n')[1:-1]]

print arg[0]