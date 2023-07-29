
l = [3, 4, 5, 6, 7, 8, 9, 10, 11]

l2 = [9, 25, 49, 81, 121]

l3 = []
for i in l:
    if i % 2 == 1:
        l3.append(i**2)
print(l3)


l4 = [i**2 for i in l if i % 2 == 1]
print(l4)


