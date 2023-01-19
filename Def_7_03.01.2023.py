def qwerty(my_str1, my_str2):
    my_list = list(my_str1)
    my_list2 = list(my_str2)
    for i in my_list:
        count_i = my_list.count(i)
        if count_i == 1:
            if i in my_list2:
                count_i = my_list2.count(i)
                if count_i == 1:
                    unique_list.append(i)
        else:
            count_i = 0
    return unique_list


my_str1 = input('Введите строку: ')
my_str2 = input('Введите строку: ')
unique_list = []
print(qwerty(my_str1, my_str2))
print()
