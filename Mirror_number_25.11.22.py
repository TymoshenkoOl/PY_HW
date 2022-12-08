three_digit_number = int(input('Введіть тризначне число: '))
first_digit = three_digit_number // 100
second_digit = three_digit_number // 10 % 10
third_digit = three_digit_number % 10
print(f'{third_digit}{second_digit}{first_digit}')


