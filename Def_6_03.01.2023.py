def qwerty(my_str1, my_str2):
    my_list = list(my_str1)
    my_list2 = list(my_str2)
    for i in my_str1:
        if i in my_str2:
            unique_list.append(i)
            if i in unique_list:
                continue
    return unique_list


my_str1 = input('Введите строку: ')
my_str2 = input('Введите строку: ')
unique_list = []
print(qwerty(my_str1, my_str2))
print()
