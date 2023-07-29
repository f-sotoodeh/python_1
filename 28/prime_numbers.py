from time import time
from math import sqrt

tic = time()
n = 100
prime_numbers = [2]
for i in range(3, n, 2):
    # for p in [j for j in prime_numbers if j <= sqrt(i)]:
    for p in prime_numbers:
        if i % p == 0:
            break
    else:
        prime_numbers.append(i)
# print(len(prime_numbers))
toc = time()
print(toc-tic)
print(prime_numbers)
