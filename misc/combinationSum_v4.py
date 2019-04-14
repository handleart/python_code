from collections import deque
def combinationSum(a, sm):
    a = [j for j in sorted(set(a)) if j <= sm]
    queue = deque([[i] for i in a])
    combos = set()
    while queue:

        cur = queue.popleft()
        print cur, queue
        
        if sum(cur) == sm:
            combos.add(tuple(sorted(cur)))
            continue
        elif sum(cur) > sm:
            continue
        for i in range(len(a)-1, -1, -1):
            if a[i] < cur[-1]:
               break
            if sum(cur) + a[i] <= sm:
                nex = cur + [a[i]]
                queue.append(nex)
    if not combos: return 'Empty'
    
    strings = ["("+' '.join([str(x) for x in c])+")" for c in sorted(combos)]
    return ''.join(strings)

a = [8, 1, 8, 6, 8]
s = 12
result = "(1 1 1 1 1 1 1 1 1 1 1 1)(1 1 1 1 1 1 6)(1 1 1 1 8)(6 6)"
print combinationSum(a, s)
                        
    