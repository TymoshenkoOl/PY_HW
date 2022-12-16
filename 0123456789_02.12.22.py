my_string = '0123456789'
start_two = 0
finish_two = 1
start_one = 0
finish_one = 1
dig_one = int(str(my_string[start_one:finish_one]))
dig_two = int(str(my_string[start_two:finish_two]))
i = int(f'{dig_one}{dig_two}')
print(i, type(i))
while dig_one <= 9:
    while dig_two != 9:
        start_two += 1
        finish_two += 1
        dig_two = int(str(my_string[start_two:finish_two]))
        i = int(f'{dig_one}{dig_two}')
        print(i, type(i))
    else:
        start_two = 0
        finish_two = 1
        dig_two = int(str(my_string[start_two:finish_two]))
        start_one += 1
        finish_one += 1
        dig_one = int(str(my_string[start_one:finish_one]))
        i = int(str(f'{dig_one}{dig_two}'))
        print(i, type(i))
