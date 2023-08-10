while True:
    try:
        n = int(input('? '))
        if n >= 10:
            raise Exception('Number greater that 9')
        a = 10 / n
        print({2.0:'TWO'}[a])
        print([9, 8, 7][int(a)])
        break
    except ValueError:
        print('You should enter a number.')
    except ZeroDivisionError:
        print('You must not enter 0.')
    except KeyError:
        print(a)
    except Exception as e:
        print(e)
        print('Something goes wrong!')

