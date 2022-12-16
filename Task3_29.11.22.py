any_digit = int(input('Введіть число: '))
if 11 < any_digit:
    if any_digit % 2 == 0 or any_digit % 3 == 0 or any_digit % 5 == 0 or any_digit % 7 == 0 or any_digit % 11 == 0:
        print('Число не є простим')
    else:
        print('Число є простим')
elif 0 < any_digit <= 11:
    if any_digit % 2 == 0 and any_digit != 2 or any_digit == 1 or any_digit % 3 == 0 and any_digit != 3:
        print('Число не є простим')
    else:
        print('Число є простим')

