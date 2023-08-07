# Dictionary
# b = {'a': 1, 'b': 2, 'c': 3}
# c = {}

# Set
# a = {1, 3, 5, 7, 9}
# d = set()


from random import randint

l = [randint(2,9) for i in range(30)]

print(l)

print()

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

# l2 = [i for i in l if i not in l2]

print(l2)

l3 = list(set(l))
print()

print(l3)
