from collections import Counter
from itertools import product

a =[]

combs = list(product('12', repeat=4))
for comb in combs:
    x = 81
    comb = ''.join((comb))
    for i in range(len(comb)):
        if comb[i] == '1':
            x = int(x/3)

        if comb[i] == '2':
            x = x*5

    a.append(x)

print(Counter(a))

