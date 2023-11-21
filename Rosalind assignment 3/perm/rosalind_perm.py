#enumerating gene order 

import math
from itertools import permutations

with open('perm_result.txt', 'w') as file:
    n = 7
    numbers = list(range(1, n + 1))
    file.write(str(math.factorial(n)))

    for perm in permutations(numbers):
        file.write(' '.join(map(str, perm)) + '\n')