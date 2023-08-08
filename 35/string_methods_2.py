
# s = 'His name is Ali. Ali is a student.'

# print(s.replace('Ali', 'Reza'))

# a = 12
# b = 34

# print(f'{a} x {b} = {a*b}')

# s = '{} x {} = {}'
# print(s.format(a, b, a*b))

# invoice = [
#     ('pen', '25,000'),
#     ('notebook', '110,000'),
# ]


# for item, price in invoice:
#     print(item.center(12), price.rjust(7))

age = input('How old are you? ')
if age.isdigit():
    age = int(age)
else:
    print('Please enter a valid age.')
