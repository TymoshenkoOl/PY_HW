end_of_range = int(input('Введіть число: '))
for i in range(1, end_of_range + 1):
    if i ** 2 <= end_of_range + 1:
        print(i ** 2, end=' ')
