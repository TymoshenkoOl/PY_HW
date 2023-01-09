any_dig = (input('Введіть число відмінне від "0": '))
try:
    any_digit = int(any_dig)
except:
    print('Не є числом')
    quit()
if any_digit == 0 or any_digit == 1:
    print('Не відноситься ні до простих ні до складених чисел')
    quit()
n = 1
k = 0
while any_digit >= n:
    if any_digit % n == 0:
        k += 1
    n += 1
if k <= 2:
    print('Число є простим')
else:
    print('Число є складеним')
