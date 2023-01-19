def qwerty(my_str):
    my_list = list(my_str)
    for i in my_list:
        if my_list.count(i) == 1:
            unique_list.append(i)
    return unique_list


my_str = input('Введите строку: ')
unique_list = []
print(qwerty())
print()
