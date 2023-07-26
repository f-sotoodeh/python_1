
l = [3, 4, 5]

l.append(6)
l.insert(1, 3.5)
l.insert(0, 2)

l2 = [9, 8, 7]

l.extend(l2)
# l += l2

l.append(3.5)

l.remove(3.5)

# while 3.5 in l:
#     l.remove(3.5)

# x = l.pop(20)

# l[3] = 100
l[3] **= 2

print(l)
# print(x)
