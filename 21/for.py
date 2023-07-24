
# l = ['aaa', 'bbb', 'ccc']
# for i in l:
#     print(i)

# c = 10
# while c > 0:
#     print('Hello')
#     c -= 1


# for _ in range(10):
#     print('Hello')


#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *


n = int(input('Enter a number: '))
for i in range(1, n+1):
    print((' '*(n-i))+('* '*i))
