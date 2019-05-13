i = 0


def hanoi(n, x, y, z):
    global i
    if n == 1:
        i += 1
        print(i, '...', x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)
        i += 1
        print(i, '...', x, '-->', z)
        hanoi(n - 1, y, x, z)


n = 20
hanoi(n, 'X', 'Y', 'Z')
print('总共需要{}步。'.format(i))  # i = 2 ** n - 1
