from collections import Counter
from itertools import product

a =[]
combs = list(product('12', repeat=3))
for comb in combs:
    x = 2
    comb = ''.join((comb))
    for i in range(len(comb)):
        if comb[i] == '1':
            x = x+2

        if comb[i] == '2':
            x = x*3

    a.append(x)

a.sort()
print(len(a))
print(Counter(a))

