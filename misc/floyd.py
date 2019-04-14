def floyd(f, x0):
    tortoise = f[x0] # f(x0) is the element/node next to x0.
    hare = f[f[x0]]
    while tortoise != hare:
        tortoise = f[tortoise]
        hare = f[f[hare]]

    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f[tortoise]
        hare = f[hare]  # Hare and tortoise move at same speed
        mu += 1

    lam = 1
    hare = f[tortoise]
    while tortoise != hare:
        hare = f[hare]
        lam += 1
 
    print lam, mu   
    return f[lam]


a = [2, 3, 3, 1, 5, 2]

print floyd(a, 1)  == 3

a = [2, 4, 3, 1, 5, 2]
print floyd(a, 1) == 2

a = [2, 4, 3, 5, 5, 2]
print floyd(a, 1) == 5

a = [5, 2, 3, 5, 5, 2]
print floyd(a, 1) == 5

a = [0, 1, 2, 3, 4, 5]
print floyd(a, 1)