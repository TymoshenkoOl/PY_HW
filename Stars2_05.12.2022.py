print('A')
end_of_range = int(input('Введіть число: '))
n = 0
for i in range(1, end_of_range + 1):
    if i == 1:
        print(' ' * (end_of_range - 1), '*' * (i + i - 1))
    elif i != 1 or i != end_of_range + 1:
        print(' ' * (end_of_range - i), '*', sep=' ', end="")
        print(' ' * (n + 1), ' ' * n, '*', sep='')
        if n == end_of_range - 3:
            print('', '*' * (i + i + 1))
            break
        else:
            n += 1
print()

print('B')
end_of_range = int(input('Введіть число: '))
for i in range(1, end_of_range + 1):
    print(' ' * (end_of_range - i), '*' * (i + i - 1))
print()

print('Bonus')
end_of_range = int(input('Введіть число: '))
n = 0
for i in range(1, end_of_range + 1):
    if i == 1:
        print(' ' * (end_of_range - 1), '*' * (i + i - 1))
    elif i != 1 or i != end_of_range + 1:
        print(' ' * (end_of_range - i), '*', sep=' ', end="")
        print(' ' * n, '*', ' ' * n, '*', sep='')
        if n == end_of_range - 3:
            print('', '*' * (i + i + 1))
            break
        else:
            n += 1
print()

print('C')
end_of_range = int(input('Введіть число: '))
for i in range(1, end_of_range + 1):
    print(' ' * (end_of_range - i), '*' * (i + i - 1))
for h in range(end_of_range - 1, 0, -1):
    if h == 1:
        print(' ' * (end_of_range - h + 1), '*', sep='')
    else:
        print(' ' * (end_of_range - h + 1), '*', sep='', end='')
        n = h + h - 3
        print(' ' * n, '*', sep='')
        n = n - 2
print()

print('D')
end_of_range = int(input('Введіть число: '))
n = end_of_range - 3
for i in range(1, end_of_range + 1):
    print(' ' * (end_of_range - i), '*' * (i + i - 1))
for h in range(end_of_range - 1, 0, -1):
    if h == 1:
        print(' ' * (end_of_range - h + 1), '*', sep='')
    else:
        print(' ' * (end_of_range - h + 1), '*', sep='', end='')
        print(' ' * n, '*', ' ' * n, '*', sep='')
        n = n - 1
print()
