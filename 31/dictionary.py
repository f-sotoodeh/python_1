#    0  1  2
l = [3, 4, 5]
a = [
    3,
    4,
    5,
]


# d = {
#     'firstname': 'Ali', 
#     'lastname': 'Alavi',
#     'phone number': '09123456789',
#     'age': 20
# }

# d = dict(
#     firstname='Ali',
# )

d = {'a': 10, 1.5:0}

d[1.5] = 20
e = {'2':30, 'x':100, 'a':5}
d.update(e)
d.update(abc=100, xyz=200)

a = d.pop('y', None)

# print(d)
# print(a)

# print(d[1.6])
print(d.get(1.6, 0))
